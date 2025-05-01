from app.models.book import Book
from sqlalchemy import select
class BookRepository:
    @staticmethod
    async def add(session,book):
        await session.add(book)
        await session.commit()

    @staticmethod
    async def get_all(session):
        result = await session.execute(select(Book))
        return result.scalars().all()

    @staticmethod
    async def get_by_id(session,book_id):
        return await session.get(Book,book_id)

    @staticmethod
    async def delete(session,book):
        await session.delete(book)
        await session.commit()