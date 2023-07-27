from pydantic import BaseModel, Field
from datetime import date
class EmployeeBase(BaseModel):
    first_name: str
    last_name :str
    start_work_year: int
    department_id : str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    first_name: str | None = None
    last_name :str | None = None
    start_work_year: int | None = None
    department_id : str | None = None
    class Config:
        orm_mode = True
class Employee(EmployeeBase):
    id: str
    class Config:
        orm_mode = True
class EmployeeDeleteResponse(BaseModel):
    message:str
    class Config:
        orm_mode = True