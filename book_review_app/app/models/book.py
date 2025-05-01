
from app.models import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String)
    year_published = Column(Integer)
    summary = Column(Text)

    reviews = relationship('Review', back_populates='book', cascade="all, delete")
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "year_published": self.year_published,
            "summary": self.summary,
        }
