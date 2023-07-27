from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from sql_app.database import SessionLocal
from schemas.shift_emp_schema import ShiftEmp,ShiftEmpCreate
from models.shift_emp_model import ShiftEmp as ShiftModel


from routers.deps import get_db
from BLL.emp_to_shift_bl import EmpToShiftBL
from .deps import check_actions
emp_to_shift_router = APIRouter(tags=["Employees Shifts"],dependencies=[Depends(check_actions)])
emp_to_shift_bl = EmpToShiftBL()



@emp_to_shift_router.get("/", response_model=list[ShiftEmp])
def read_emp_to_shifts(db: Session = Depends(get_db)):
    emp_to_shifts = emp_to_shift_bl.get_all_emp_shifts(db)
    return emp_to_shifts


@emp_to_shift_router.get("/{emp_to_shift_id}", response_model=ShiftEmp)
def read_emp_to_shift(emp_to_shift_id: str, db: Session = Depends(get_db)):
    emp_to_shift = emp_to_shift_bl.get_emp_shift(db, emp_shift_id=emp_to_shift_id)
    if emp_to_shift is None:
        raise HTTPException(status_code=404, detail="ShiftEmp not found")
    return emp_to_shift


@emp_to_shift_router.post("/", response_model=ShiftEmp)
def create_emp_to_shift(shift_emp: ShiftEmpCreate, db: Session = Depends(get_db)):
    return emp_to_shift_bl.add_emp_shift(db,emp_shift_obj=shift_emp)


""" 
@emp_to_shift_router.delete("/{emp_to_shift_id}")
def delete_emp_to_shift(emp_to_shift_id: str, db: Session = Depends(get_db)):
    deleted_emp_to_shift = emp_to_shift_bl.delete_emp_to_shift(db, emp_to_shift_id=emp_to_shift_id)
    if deleted_emp_to_shift is None:
        raise HTTPException(status_code=404, detail="ShiftEmp not found")
    return deleted_emp_to_shift """