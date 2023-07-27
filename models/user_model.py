from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import uuid
from sql_app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True,default=uuid.uuid4, nullable=False)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String)
    num_of_actions = Column(Integer)