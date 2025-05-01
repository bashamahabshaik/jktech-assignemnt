from app.models.review import Review
from sqlalchemy import select
class ReviewRepository:
    @staticmethod
    async def add(session,review):
        session.add(review)
        await session.commit()

    @staticmethod
    async def get_by_book_id(session,book_id):
        stmt = select(Review).filter_by(book_id=book_id)
        result = await session.execute(stmt)
        return result.scalars().all()
