from sqlalchemy.orm import Session

from schemas.department_schema import DepartmentCreate, DepartmentUpdate, DepartmentDeleteResponse
from models.department_model import Department
from routers.deps import get_db
from fastapi import  Depends
class DepartmentDBDAL:
    
    def get_department(self, db: Session, department_id: str):
        return db.query(Department).filter(Department.id == department_id).first()

    def get_departments(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Department).all()
    
    def add_department(self, db: Session, department: DepartmentCreate):
        db_department = Department(**department.model_dump())
        db.add(db_department)
        db.commit()
        db.refresh(db_department)
        return db_department

    def update_department(self, db: Session, department_id: str, department: DepartmentUpdate):
        db_department = db.query(Department).filter(Department.id == department_id).first()
        if db_department:
            for key, value in department.dict(exclude_unset=True).items():
                setattr(db_department, key, value)
            db.add(db_department)
            db.commit()
            db.refresh(db_department)
        return db_department
    
    def delete_department(self, db:Session, department_id:str) -> dict | None: 
        db_department = db.query(Department).filter(Department.id == department_id).first()
        dept_name = db_department.name
        
        if db_department:
            db.delete(db_department)
            db.commit()
            return {"message": f"Department {dept_name} deleted"}
        else:
            return None

department_db_dal = DepartmentDBDAL()