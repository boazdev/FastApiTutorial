from typing import Annotated
from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from routers.auth_router import auth_router
from routers.user_router import user_router
from routers.shift_router import shift_router
from routers.employee_router import employee_router   
from routers.department_router import department_router
from routers.cheat_router import cheat_router
from routers.emp_to_shift_router import emp_to_shift_router
from sql_app.db_utils import *

app = FastAPI()
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with a list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Replace "*" with a list of allowed HTTP methods
    allow_headers=["*"],  # Replace "*" with a list of allowed headers
)
app.include_router(cheat_router,prefix="/cheat")
app.include_router(auth_router,prefix="/auth")
app.include_router(user_router,prefix="/user")
app.include_router(shift_router,prefix="/shift")
app.include_router(employee_router,prefix="/employee")
app.include_router(department_router,prefix="/department")
app.include_router(emp_to_shift_router,prefix="/emp_to_shift")