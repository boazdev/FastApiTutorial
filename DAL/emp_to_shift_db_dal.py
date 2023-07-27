from sqlalchemy.orm import Session

from schemas.shift_emp_schema import ShiftEmpCreate
from models.shift_emp_model import ShiftEmp
class EmpToShiftDBDAL:
    def __init__(self):
        pass

    def get_emp_to_shift(self,db:Session,id:str): #get 
         return db.query(ShiftEmp).filter(ShiftEmp.id == id).first()
    
    def get_all_emp_to_shifts(self, db:Session):
        return db.query(ShiftEmp).all()
        

    def add_emp_to_shift(self,db:Session, emp_shift: ShiftEmpCreate):
        db_emp_shift = ShiftEmp(**emp_shift.model_dump())
        db.add(db_emp_shift)
        db.commit()
        db.refresh(db_emp_shift)
        return db_emp_shift

emp_to_shift_db_dal = EmpToShiftDBDAL()        

    