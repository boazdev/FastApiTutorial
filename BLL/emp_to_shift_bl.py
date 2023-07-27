from DAL.emp_to_shift_db_dal import EmpToShiftDBDAL

from schemas.shift_emp_schema import ShiftEmp,ShiftEmpCreate
from sqlalchemy.orm import Session
class EmpToShiftBL():
    def __init__(self):
        self.__emp_shift_db_dal = EmpToShiftDBDAL()

    def get_all_emp_shifts(self, db:Session):
        return self.__emp_shift_db_dal.get_all_emp_to_shifts(db)
    
    """ def get_all_employees_aggr(self, db:Session): #get all employees, in each employee row should be dept_id and dept name, and list of shifts
        return self.__employee_db_dal.get_employees_aggr(db) """

    def get_emp_shift(self, db:Session, emp_shift_id:str):
        return self.__emp_shift_db_dal.get_emp_to_shift(db,emp_shift_id)#(db,emp_shift_id)
    
    def add_emp_shift(self,db:Session, emp_shift_obj:ShiftEmpCreate):
        return self.__emp_shift_db_dal.add_emp_to_shift(db,emp_shift_obj)
 
   
    """ def delete_employee(self, db:Session, employee_id:str):
        return self.__employee_db_dal.delete_employee(db=db,employee_id=employee_id) """