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

class UserUpdate(BaseModel):
    full_name : str | None = None
    password : str | None = None
    num_of_actions: int | None = None
class User(UserBase):
    id: str
    

    class Config:
        orm_mode = True