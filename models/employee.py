from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Employee(Base):
__tablename__ = "employees"


id = Column(Integer, primary_key=True)
name = Column(String)
designation = Column(String)
page_id = Column(Integer, ForeignKey("linkedin_pages.id"))


page = relationship("LinkedInPage", back_populates="employees")