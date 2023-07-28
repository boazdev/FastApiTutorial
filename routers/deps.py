from typing import Generator
from jose import jwt,JWTError
from fastapi import Depends, HTTPException, status , Request
from settings import config
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from pydantic import ValidationError
from BLL.action_bl import ActionBL
from sql_app.database import SessionLocal


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
settings = config.get_settings()
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def create_access_token(data: dict):
    to_encode = data.copy()
    
    encoded_jwt = jwt.encode(data, key=settings.jwt_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt

def verify_token(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    payload=None
    try:
        payload = jwt.decode(
            token, key=settings.jwt_key, algorithms=[settings.jwt_algorithm],
        )
        token_data = payload
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    """ print("verify token payload:")
    print(payload) """
    return payload

def is_action_path(path):
    return True

def check_actions(
    request: Request,
    payload: dict = Depends(verify_token),
    db: Session = Depends(get_db)
):
    user_id = payload.get("sub")
    action_path = request.url.path
    """ print(f"check actions,  user id: {user_id}, action path: {action_path}") """
    is_action_path = True
    if is_action_path:
        action_bl = ActionBL()
        action_result = action_bl.add_action(db=db,user_id=user_id)
        if action_result == None:
            raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="User out of actions",
        )
        
    """ if is_action_path:
        create_action_record(db, user_id)
        max_allowed_actions = 5
        todays_actions = get_todays_actions(db, user_id)

        if len(todays_actions) >= max_allowed_actions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You have exceeded the maximum allowed actions for today.",
            ) """
""" def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user """