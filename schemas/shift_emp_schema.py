from pydantic import BaseModel, Field
class ShiftEmpBase(BaseModel):
    shift_id:str
    employee_id:str

class ShiftEmpCreate(ShiftEmpBase):
    pass

class ShiftEmp(ShiftEmpBase):
    id: str
    class Config:
        orm_mode = True