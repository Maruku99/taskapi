from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    status = Column(String, default="open")
    owner_id = Column(Integer, ForeignKey("users.id"))
    # relationship to user
    owner = relationship("User", back_populates="tasks")
