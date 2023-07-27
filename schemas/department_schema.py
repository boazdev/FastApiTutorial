from pydantic import BaseModel, Field
from datetime import date
class DepartmentBase(BaseModel):
    name: str
    manager_id : str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    name: str | None = None
    manager_id : str | None = None

class Department(DepartmentBase):
    id: str
    class Config:
        orm_mode = True

class DepartmentDeleteResponse(BaseModel):
    message:str
    class Config:
        orm_mode = True