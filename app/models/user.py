from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    hash_password = Column(String, nullable=False)
    role = Column(String, default="user")
    # relationship to tasks
    tasks = relationship("Task", back_populates="owner")
