from sqlalchemy.orm import Session

from schemas.action_schema import ActionCreate
from models.action_model import Action

class ActionDBDAL:
    
    def get_action(self, db: Session, action_id: str):
        return db.query(Action).filter(Action.id == action_id).first()

    def get_all_actions(self, db: Session):
        return db.query(Action).all()
    
    def add_action(self, db: Session, action: ActionCreate): #add action to user_id
        db_action = Action(**action.model_dump())
        db.add(db_action)
        db.commit()
        db.refresh(db_action)
        return db_action



action_db_dal = ActionDBDAL()