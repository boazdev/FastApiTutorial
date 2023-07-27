from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    full_name: str
    num_of_actions:int

class UserLogin(BaseModel):
    username: str
    password: str
    
class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str
    

    class Config:
        orm_mode = True