from sqlalchemy.orm import Session
from sqlalchemy import select, literal_column
from schemas.employee_schema import EmployeeCreate, EmployeeUpdate, EmployeeDeleteResponse
from models.employee_model import Employee
from models.department_model import Department
from models.shift_emp_model import ShiftEmp
from models.shift_model import Shift
from routers.deps import get_db
from fastapi import  Depends
class EmployeeDBDAL:
    def __init__(self, db2: Session = None):
        self.__db = db2

    def get_employee(self, db: Session, employee_id: str):
        return db.query(Employee).filter(Employee.id == employee_id).first()

    def get_employees(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Employee).offset(skip).limit(limit).all()
    
    def get_employees_aggr(self, db: Session):
        stmt = select(Employee.id, Employee.first_name, Employee.last_name, Employee.start_work_year,
                  Employee.department_id, Department.name, Shift.date_time, Shift.starting_hour, Shift.ending_hour)
        stmt = stmt.select_from(Employee).join(Department, Employee.department_id == Department.id)
        stmt = stmt.join(ShiftEmp, Employee.id == ShiftEmp.employee_id)
        stmt = stmt.join(Shift, ShiftEmp.shift_id== Shift.id)
        """ stmt = stmt.group_by("Employee.id") """
        result = db.execute(stmt).fetchall()
        return result
        """ employees = [
        {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "start_work_year": row[3],
            "department_id": row[4],
            "department_name": row[5],
            "shift_date":row[6],
            "shift_starting_hour":row[7],
            "shift_ending_hour":row[8]
        }
        for row in result
        ]
        return employees """
    
    def get_employees_aggr_old(self, db: Session):
        stmt = select(Employee.id, Employee.first_name, Employee.last_name, Employee.start_work_year,
                  Employee.department_id, Department.name)
        stmt = stmt.select_from(Employee).join(Department, Employee.department_id == Department.id)
        result = db.execute(stmt).fetchall()
        employees = [
        {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "start_work_year": row[3],
            "department_id": row[4],
            "department_name": row[5]
        }
        for row in result
        ]
        return employees    
    
    def get_employees_test(self, db:Session, skip: int = 0, limit: int = 100):
        return db.query(Employee).offset(skip).limit(limit).all()

    def create_employee(self, db: Session, employee: EmployeeCreate):
        db_employee = Employee(**employee.model_dump())
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    
    def update_employee(self, db: Session, employee_id: str, employee: EmployeeUpdate):
        db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if db_employee:
            for key, value in employee.model_dump(exclude_unset=True).items():
                setattr(db_employee, key, value)
           
            db.add(db_employee)
            db.commit()
            db.refresh(db_employee)
        return db_employee
    
    def delete_employee(self, db:Session, employee_id:str) -> dict | None: 
        db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
        emp_name = db_employee.first_name +" " + db_employee.last_name
        print(emp_name)
        if db_employee:
            db.delete(db_employee)
            db.commit()
            return {"message": f"Employee {emp_name} deleted"}
        else:
            return None

employee_db_dal = EmployeeDBDAL()