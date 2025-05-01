from app.models.book import Book
from app.repositories.book_repository import BookRepository
from app.db import async_session
from app.utils.llama3_client import Llama3Client


class BookService:
    llm_client = None  
    def __init__(self):
        self.llm_client = Llama3Client()
    async def create_book(self, data):
        async with async_session() as session:
            book = Book(**data)
            await BookRepository.add(session,book)
            return book
        

    async def get_books(self):
        async with async_session() as session:
            books = await BookRepository.get_all(session)
            return books

    async def get_book(self, book_id):
        async with async_session() as session:
            book = await BookRepository.get_by_id(session,book_id)
            if not book:
                raise Exception("Book not found")
            return book
    async def generate_book_summary(self, book_content):
        summary = await self.llm_client.generate_summary(book_content)
        return summary
    def update_book(self, book, data):
        for k, v in data.items():
            setattr(book, k, v)
        BookRepository.add(book)
        return book

    def delete_book(self, book):
        BookRepository.delete(book)