from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    likes = Column(Integer, default=0)

    page_id = Column(Integer, ForeignKey("linkedin_pages.id"))
    page = relationship("LinkedInPage", back_populates="posts")
