from app.models.review import Review
from app.repositories.review_repository import ReviewRepository
from app.db import async_session
class ReviewService:
    async def create_review(self, book_id, data):
        async with async_session() as session:
            data.pop("book_id", None)
            review = Review(book_id=book_id, **data)
            await ReviewRepository.add(session,review)
            return review

    async def get_reviews_for_book(self, book_id):
        async with async_session() as session:
            reviews = await ReviewRepository.get_by_book_id(session,book_id)
            if not reviews:
                raise Exception("No reviews found for this book")
            return reviews