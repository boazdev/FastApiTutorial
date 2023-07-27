from pydantic import BaseModel
from datetime import date

class ActionBase(BaseModel):
    max_actions: int
    date: date
    actions_allowed: int
    user_id: str
class ActionCreate(ActionBase):
    pass

class Action(ActionBase):
    id: str

    class Config:
        orm_mode = True