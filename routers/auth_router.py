from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from routers.deps import get_db, create_access_token
""" from schemas.user_schema import UserLogin """
from DAL.user_db_dal import user_db_dal
from typing import Annotated
from models.user_model import User
auth_router = APIRouter(tags=["authorization"])

@auth_router.post("/login")
def login( form_data: Annotated[OAuth2PasswordRequestForm, Depends()],db: Session = Depends(get_db), ):
    user_info = user_db_dal.get_user_by_username(db,form_data.username)
    #print(user_info.password)
    if not user_info:
        raise HTTPException(status_code=400, detail="Incorrect username")
    if user_info.password!=form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    access_token = create_access_token(
        data={"sub": user_info.id}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.get("/logout")
def logout():
    # Handle logout logic
    return {"login":"called logout"}
