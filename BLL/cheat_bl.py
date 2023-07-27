from sqlalchemy.orm import Session
from DAL.department_db_dal import department_db_dal
from DAL.employee_db_dal import employee_db_dal
from DAL.emp_to_shift_db_dal import emp_to_shift_db_dal
from DAL.shift_db_dal import shift_db_dal
from schemas.employee_schema import EmployeeUpdate,Employee
from schemas.department_schema import DepartmentUpdate
from schemas.shift_emp_schema import ShiftEmpCreate

import random
from fastapi.encoders import jsonable_encoder
class CheatBL:
    def __init__(self) -> None:
        self.__employee_db_dal = employee_db_dal
        self.__department_db_dal = department_db_dal
        self.__emp_to_shift_db_dal = emp_to_shift_db_dal
        self.__shift_db_dal = shift_db_dal

    def fix_employee_depid(self, db:Session):
        emp_list = self.__employee_db_dal.get_employees(db)
        dept_list = self.__department_db_dal.get_departments(db)
        for emp in emp_list:
            # Choose a random department_id from dept_list
            random_dept_id = random.choice(dept_list).id
            """ print("emp name",emp.first_name) """
            # Assign the random department_id to the employee
            emp.department_id = random_dept_id
            emp_updt = EmployeeUpdate(**jsonable_encoder(emp))
           
            self.__employee_db_dal.update_employee(db,emp.id,emp_updt)
        return {"message":"success"}
    
    def fix_department_manager_id(self, db:Session):
        emp_list = self.__employee_db_dal.get_employees(db)
        dept_list = self.__department_db_dal.get_departments(db)
        for dept in dept_list:
            print(f"dept name: {dept.name}")
            print("dept workers:")
            dept_emps = list(filter(lambda item:item.department_id==dept.id,emp_list))
            random_emp_id = random.choice(dept_emps).id
            dept.manager_id= random_emp_id
            dept_updt = DepartmentUpdate(**jsonable_encoder(dept))
            self.__department_db_dal.update_department(db,dept.id,dept_updt)
            """ for emp in dept_emps:
                print(f"{emp.first_name} {emp.last_name}") """
        return {"message":"success2"}
    
    def add_employees_to_shift(self, db:Session):
        emp_list = self.__employee_db_dal.get_employees(db)
        shift_list = self.__shift_db_dal.get_shifts(db=db)
        for emp in emp_list:
             # Generate a list of four unique random shifts for the employee
            random_shifts = random.sample(shift_list, 4)

            # Add each shift to the ShiftEmp table for the employee
            for shift in random_shifts:
                shift_emp_data = ShiftEmpCreate(shift_id=shift.id, employee_id=emp.id)
                self.__emp_to_shift_db_dal.add_emp_to_shift(db, shift_emp_data)
        return {"message":"success3"}