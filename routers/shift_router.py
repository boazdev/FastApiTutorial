from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from sql_app.database import SessionLocal
from schemas.shift_schema import Shift, ShiftCreate, ShiftUpdate
from models.shift_model import Shift as ShiftModel
from DAL.shift_db_dal import shift_db_dal
from routers.deps import check_actions
shift_router = APIRouter(tags=["shift"],dependencies=[Depends(check_actions)])



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@shift_router.get("/", response_model=list[Shift])
def read_shifts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shifts = shift_db_dal.get_shifts(db, skip=skip, limit=limit)
    return shifts


@shift_router.get("/{shift_id}", response_model=Shift)
def read_shift(shift_id: str, db: Session = Depends(get_db)):
    shift = shift_db_dal.get_shift(db, shift_id=shift_id)
    if shift is None:
        raise HTTPException(status_code=404, detail="Shift not found")
    return shift


@shift_router.post("/", response_model=Shift)
def create_shift(shift: ShiftCreate, db: Session = Depends(get_db)):
    if shift.ending_hour <= shift.starting_hour:
        raise HTTPException(status_code=422, detail="Ending hour must be greater than starting hour")
    return shift_db_dal.create_shift(db, shift=shift)


@shift_router.put("/{shift_id}", response_model=Shift)
def update_shift(shift_id: str, shift: ShiftUpdate, db: Session = Depends(get_db)):
    updated_shift = shift_db_dal.update_shift(db, shift_id=shift_id, shift=shift)
    if updated_shift is None:
        raise HTTPException(status_code=404, detail="Shift not found")
    return updated_shift

@shift_router.delete("/{shift_id}", response_model=dict , tags=["Testing"])
def delete_shift(shift_id: str,  db: Session = Depends(get_db)):
    deleted_shift = shift_db_dal.delete_shift(db, shift_id=shift_id)
    if deleted_shift is None:
        raise HTTPException(status_code=404, detail="Shift not found")
    return deleted_shift