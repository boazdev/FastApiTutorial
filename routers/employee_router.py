from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from sql_app.database import SessionLocal
from schemas.employee_schema import Employee, EmployeeCreate, EmployeeUpdate , EmployeeDeleteResponse
from models.employee_model import Employee as EmployeeModel

from DAL.employee_db_dal import employee_db_dal
from routers.deps import check_actions, verify_token
from routers.deps import get_db
from BLL.employee_bl import *


employee_router = APIRouter(tags=["employee"],dependencies=[Depends(check_actions)])
employee_bl = EmployeeBL()


""" @employee_router.get("/testbl/", response_model=list[Employee])
def get_employee_by_fname(db: Session = Depends(get_db)):
    employees = employee_bl.get_all_employees(db)
    return employees """

""" def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), payload = Depends(verify_token)): """

@employee_router.get("/", response_model=list[Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = employee_db_dal.get_employees(db, skip=skip, limit=limit)
    return employees

@employee_router.get("/deps", response_model=list[dict]) #get all employees in main page that is employees.html
def read_employees_aggr( db: Session = Depends(get_db)):
    employees = employee_bl.get_all_employees_aggr(db)
    return employees


@employee_router.get("/{employee_id}", response_model=Employee)
def read_employee(employee_id: str, db: Session = Depends(get_db)):
    employee = employee_db_dal.get_employee(db, employee_id=employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@employee_router.post("/", response_model=Employee)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return employee_db_dal.create_employee(db, employee=employee)


@employee_router.put("/{employee_id}", response_model=Employee )
def update_employee(employee_id: str, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    updated_employee = employee_db_dal.update_employee(db, employee_id=employee_id, employee=employee)
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

@employee_router.delete("/{employee_id}")
def delete_employee(employee_id: str, db: Session = Depends(get_db)):
    deleted_employee = employee_db_dal.delete_employee(db, employee_id=employee_id)
    if deleted_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return deleted_employee