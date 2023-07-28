from DAL.action_db_dal import action_db_dal
from schemas.action_schema import  ActionCreate
from sqlalchemy.orm import Session
from DAL.user_db_dal import user_db_dal
from models.user_model import User
from datetime import datetime
from models.action_model import Action
class ActionBL():
    def __init__(self):
        self.__action_db_dal = action_db_dal
        self.__user_db_dal = user_db_dal
    def get_all_actions(self, db:Session):
        return self.__action_db_dal.get_actions(db)
    
    def get_action(self, db:Session, action_id:str):
        return self.__action_db_dal.get_action(db=db,action_id=action_id)
    
    def add_action(self, db:Session,user_id:str)->Action | None: #add action to user_id, #get max actions from user, get curr actions from actions
        actions_data = self.__user_db_dal.get_user_actions(db=db, user_id=user_id)
       
        
        
        actions_allowed= actions_data["max_actions"] - actions_data["action_count"] -1
        """ print("actions allowed:",actions_allowed) """
        if(actions_allowed==0):
            return None
        curr_date = datetime.now().strftime("%Y-%m-%d")
        new_action = ActionCreate(user_id=user_id,date=curr_date,
                                   max_actions=actions_data["max_actions"], actions_allowed=actions_allowed)
        return self.__action_db_dal.add_action(db=db,action=new_action)

  