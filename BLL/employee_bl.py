from DAL.employee_db_dal import employee_db_dal
from schemas.employee_schema import EmployeeUpdate
from sqlalchemy.orm import Session
from collections import defaultdict
class EmployeeBL():
    def __init__(self):
        self.__employee_db_dal = employee_db_dal

    def get_all_employees(self, db:Session, is_join: bool):
        return self.__employee_db_dal.get_employees_test(db)
    
    def get_all_employees_aggr(self, db: Session):
        result = self.__employee_db_dal.get_employees_aggr(db)
        employees_shifts = defaultdict(list)
        employees_info = {}

        for row in result:
            employee_id = row[0]
            shift = {
                "shift_date": row[6],
                "shift_starting_hour": row[7],
                "shift_ending_hour": row[8]
            }
            employees_shifts[employee_id].append(shift)

            if employee_id not in employees_info:
                employees_info[employee_id] = {
                    "id": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "start_work_year": row[3],
                    "department_id": row[4],
                    "department_name": row[5],
                }

        employees = [
            {
                "id": employee_info["id"],
                "first_name": employee_info["first_name"],
                "last_name": employee_info["last_name"],
                "start_work_year": employee_info["start_work_year"],
                "department_id": employee_info["department_id"],
                "department_name": employee_info["department_name"],
                "shifts": employees_shifts.get(employee_id, [])
            }
            for employee_id, employee_info in employees_info.items()
        ]

        return employees

    def get_employee(self, db:Session, employee_id:str):
        return self.__employee_db_dal.get_employee(db,employee_id)
    
    def update_employee(self, db:Session, employee_id:str, employee:EmployeeUpdate):
        return self.__employee_db_dal.update_employee(db=db, employee_id=employee_id, employee=employee)

    def delete_employee(self, db:Session, employee_id:str):
        return self.__employee_db_dal.delete_employee(db=db,employee_id=employee_id)