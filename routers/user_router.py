from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
""" from sql_app import crud, models, schemas """
from schemas import user_schema
from sql_app.database import SessionLocal, engine
from DAL.user_db_dal import user_db_dal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


user_router = APIRouter(tags=["user"])


@user_router.get("/", response_model=list[user_schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_db_dal.get_users(db, skip=skip, limit=limit)
    return users


@user_router.post("/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_db_dal.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return user_db_dal.create_user(db=db, user=user)

@user_router.get("/username/{username}") #todo: comment this should not be public
def read_user(username: str, db: Session = Depends(get_db)):
    db_user = user_db_dal.get_user_by_username(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.get("/{user_id}", response_model=user_schema.User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = user_db_dal.get_user_by_id(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user