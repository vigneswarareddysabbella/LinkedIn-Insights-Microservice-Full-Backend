from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .base import Base


class LinkedInPage(Base):
__tablename__ = "linkedin_pages"


id = Column(Integer, primary_key=True, index=True)
page_id = Column(String, unique=True, index=True)
name = Column(String)
url = Column(String)
industry = Column(String)
followers = Column(Integer)
description = Column(Text)
website = Column(String)
profile_pic = Column(String)
head_count = Column(Integer)


posts = relationship("Post", back_populates="page")
employees = relationship("Employee", back_populates="page")