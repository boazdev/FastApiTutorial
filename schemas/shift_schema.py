from pydantic import BaseModel, Field
from datetime import date
class ShiftBase(BaseModel):
    date_time: date
    starting_hour: int = Field(ge=0,lt=24, description="the hour must be greater or equal to zero")
    ending_hour: int = Field(ge=0,lt=24, description="the hour must be lower than 24")

class ShiftCreate(ShiftBase):
    pass

class ShiftUpdate(ShiftBase):
    pass

class Shift(ShiftBase):
    id: str

    class Config:
        orm_mode = True