from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sql_app.database import Base
import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .department_model import Employee

class Department(Base):
    __tablename__ = "department"
    
    id = Column(String, primary_key=True, index=True, default=uuid.uuid4, nullable=False)
    name = Column(String)
    manager_id = Column(String, ForeignKey('employee.id'))
    
    # Define a relationship to the Employee model
    """ employees = relationship("Employee", back_populates="department")

    # Define a relationship to the Employee model for the manager
    manager = relationship("Employee", back_populates="managed_department", uselist=False) """
