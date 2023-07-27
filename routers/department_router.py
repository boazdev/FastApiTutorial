from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from sql_app.database import SessionLocal
from schemas.department_schema import Department, DepartmentCreate, DepartmentUpdate , DepartmentDeleteResponse
from models.department_model import Department as DepartmentModel
from .deps import verify_token,check_actions
department_router = APIRouter(tags=["department"] ,dependencies=[Depends(check_actions)])
from routers.deps import get_db
from BLL.department_bl import *
department_bl = DepartmentBL()




@department_router.get("/", response_model=list[Department])
def read_departments(db: Session = Depends(get_db)):
    departments = department_bl.get_all_departments(db)
    return departments


@department_router.get("/{department_id}", response_model=Department)
def read_department(department_id: str, db: Session = Depends(get_db)):
    department = department_bl.get_department(db, department_id=department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department


@department_router.post("/", response_model=Department)
def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    return department_bl.add_department(db, department=department)


@department_router.put("/{department_id}", response_model=Department)
def update_department(department_id: str, department: DepartmentUpdate, db: Session = Depends(get_db)):
    updated_department = department_bl.update_department(db, department_id=department_id, department=department)
    if updated_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return updated_department

@department_router.delete("/{department_id}")
def delete_department(department_id: str, db: Session = Depends(get_db)):
    deleted_department = department_bl.delete_department(db, department_id=department_id)
    if deleted_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return deleted_department