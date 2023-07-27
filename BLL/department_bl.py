from DAL.department_db_dal import department_db_dal
from schemas.department_schema import DepartmentUpdate, DepartmentCreate
from sqlalchemy.orm import Session
class DepartmentBL():
    def __init__(self):
        self.__department_db_dal = department_db_dal

    def get_all_departments(self, db:Session):
        return self.__department_db_dal.get_departments(db)
    
    def get_department(self, db:Session, department_id:str):
        return self.__department_db_dal.get_department(db=db,department_id=department_id)
    
    def add_department(self, db:Session,department:DepartmentCreate):
        return self.__department_db_dal.add_department(db=db,department=department)

    def update_department(self, db:Session, department_id:str, department:DepartmentUpdate):
        return self.__department_db_dal.update_department(db=db, department_id=department_id, department=department)

    def delete_department(self, db:Session, department_id:str):
        return self.__department_db_dal.delete_department(db=db,department_id=department_id)