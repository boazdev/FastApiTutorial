from sqlalchemy.orm import Session

from schemas.shift_schema import ShiftCreate, ShiftUpdate
from models.shift_model import Shift

class ShiftDBDAL:
    def __init__(self, db2: Session = None):
        self.__db = db2

    def get_shift(self, db: Session, shift_id: str):
        return db.query(Shift).filter(Shift.id == shift_id).first()

    def get_shifts(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Shift).offset(skip).limit(limit).all()

    def create_shift(self, db: Session, shift: ShiftCreate):
        db_shift = Shift(**shift.model_dump())
        db.add(db_shift)
        db.commit()
        db.refresh(db_shift)
        return db_shift

    def update_shift(self, db: Session, shift_id: str, shift: ShiftUpdate):
        db_shift = db.query(Shift).filter(Shift.id == shift_id).first()
        if db_shift:
            for key, value in shift.dict(exclude_unset=True).items():
                setattr(db_shift, key, value)
            db.add(db_shift)
            db.commit()
            db.refresh(db_shift)
        return db_shift
shift_db_dal = ShiftDBDAL()