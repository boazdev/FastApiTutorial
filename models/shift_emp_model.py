from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sql_app.database import Base
import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .department_model import Department


class ShiftEmp(Base):
    __tablename__ = "shift_employee" #todo: add foreign key
    
    id = Column(String, primary_key=True, index=True, default=uuid.uuid4, nullable=False)
    shift_id = Column(String, ForeignKey('shift.id'))
    employee_id = Column(String, ForeignKey('employee.id'))
    
    # Define a relationship to the Department model
    """ department = relationship("Department", back_populates="employees",foreign_keys=[department_id])

    # Define a relationship to the Department model for the managed department
    managed_department = relationship("Department", back_populates="manager", uselist=False,foreign_keys="" ) """