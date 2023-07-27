from sqlalchemy import Column, Integer, DateTime, String, ForeignKey,Date
from sqlalchemy.orm import relationship
import uuid
from sql_app.database import Base

class Shift(Base):
    __tablename__ = "shift"

    id = Column(String, primary_key=True, index=True, default=uuid.uuid4, nullable=False)
    date_time = Column(Date)
    starting_hour = Column(Integer)
    ending_hour = Column(Integer)