from sql_app.database import SessionLocal
""" from schemas.department_schema import Department, DepartmentCreate, DepartmentUpdate , DepartmentDeleteResponse
from models.department_model import Department as DepartmentModel """
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
cheat_router = APIRouter(tags=["cheats"])
from routers.deps import get_db
from BLL.cheat_bl import *
cheat_bl = CheatBL()

@cheat_router.get("/{func_name}")
def call_cheat_func(func_name: str, db: Session = Depends(get_db)):
    # Check if the function exists in CheatBL
    if hasattr(cheat_bl, func_name) and callable(getattr(cheat_bl, func_name)):
        # Call the function and return the result
        func = getattr(cheat_bl, func_name)
        return func(db)
    else:
        return {"message":f"Function '{func_name}' not found in CheatBL."}