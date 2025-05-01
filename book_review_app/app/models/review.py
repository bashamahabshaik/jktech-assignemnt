# from app.db import db
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.models import Base
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(String, nullable=False)
    review_text = Column(Text)
    rating = Column(Integer)

    book = relationship('Book', back_populates='reviews')
    
    def to_dict(self):
        return {
            "id": self.id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "review_text": self.review_text,
            "rating": self.rating,
        }
