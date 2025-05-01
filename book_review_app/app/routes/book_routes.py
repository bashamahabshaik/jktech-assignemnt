from flask import Blueprint, request, jsonify
from app.services.book_service import BookService
from app.services.review_service import ReviewService
from app.utils.llama3_client import Llama3Client
bp = Blueprint('books', __name__, url_prefix='/books')
book_service = BookService()
review_service = ReviewService()
llm_client = Llama3Client()

@bp.route('', methods=['POST'])
async def create_book():
    data = request.json
    book = await book_service.create_book(data)
    return jsonify(id=book.id), 201

@bp.route('', methods=['GET'])
async def list_books():
    books = await book_service.get_books()
    return jsonify([b.to_dict() for b in books])

@bp.route('/<int:book_id>', methods=['GET'])
async def get_book(book_id):
    book = await book_service.get_book(book_id)
    return jsonify(book.to_dict()) if book else ('Not found', 404)

@bp.route('/<int:book_id>/summary', methods=['GET'])
async def get_book_summary(book_id):
    book = await book_service.get_book(book_id)
    if not book:
        return ('Not found', 404)
    summary = await book_service.generate_book_summary(book.summary)
    reviews = await review_service.get_reviews_for_book(book_id)
    if reviews:
        average_rating = sum([review.rating for review in reviews]) / len(reviews)
    else:
        average_rating = 0
    return jsonify({
        'book': {
            'title': book.title,
            'author': book.author,
            'genre': book.genre,
            'summary': summary,
            'average_rating': round(average_rating)
        }
    })
    
@bp.route('/recommendations', methods=['GET'])
async def get_book_recommendations():
    preferences = {k: request.args[k] for k in request.args}
    books = await book_service.get_books()
    book_list = [
        f"{b.title} by {b.author} ({b.genre})"
        for b in books
    ]
    recommendations = await llm_client.generate_recommendations(preferences, book_list)
    
    return jsonify({
        "ai_recommendations": recommendations
    })