from sqlalchemy.orm import Session
from sqlalchemy import func,select, join
#from sql_app import models, schemas
from schemas.user_schema import *
from models.user_model import User
from schemas.user_schema import UserCreate,UserLogin
from models.action_model import Action


class UserDBDAL:
    def __init__(self, db2: Session = None):
        self.__db = db2


    def get_user(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()


    def get_user_by_username(self, db: Session, username: str)->User: 
        return db.query(User).filter(User.username == username).first()


    def get_user_by_id(self, db: Session, id: str):
        return db.query(User).filter(User.id == id).first()

    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()

    def get_user_actions(self, db: Session, user_id: str) -> dict:
        subquery = (
            select(
                Action.user_id,
                func.count(Action.id).label("action_count")
            )
            .where(Action.date == func.curdate())
            .group_by(Action.user_id)
            .alias()
        )

        stmt = (
            select(
                User.id,
                User.num_of_actions,
                func.coalesce(subquery.c.action_count, 0).label("action_count")
            )
            .select_from(User)
            .outerjoin(subquery, User.id == subquery.c.user_id)
            .where(User.id == user_id)
        )

        result = db.execute(stmt).fetchall()

        if not result:
            return {
                "user_id": None,
                "max_actions": None,
                "action_count": 0,
            }

        user_actions = {
            "user_id": result[0][0],
            "max_actions": result[0][1],
            "action_count": result[0][2],
        }

        return user_actions
    
    """ def get_user_actions2(self, db:Session, user_id:str)->dict: 
        stmt = (
        select(User.id,User.num_of_actions, func.count(Action.id).label("action_count"))
        .select_from(User)
        .outerjoin(Action, User.id == Action.user_id)
        .where(User.id == user_id)
        .where(Action.date == func.current_date())
        )

        result = db.execute(stmt).fetchall()

        if not result:
            return {
                "max_actions": None,
                "action_count": 0,
            }

        user_actions = {
            "max_actions": result[0][1],
            "action_count": result[0][2],
        }

        return user_actions """

    def create_user(self, db: Session, user: UserCreate):
        password = user.password
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
user_db_dal = UserDBDAL()