import uuid
from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sql_app.database import Base

class Action(Base):
    __tablename__ = "action"

    id = Column(String(36), primary_key=True, index=True, default=uuid.uuid4, nullable=False)
    max_actions = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    actions_allowed = Column(Integer, nullable=False)
    user_id = Column(String(36), ForeignKey("user.id"), nullable=False)