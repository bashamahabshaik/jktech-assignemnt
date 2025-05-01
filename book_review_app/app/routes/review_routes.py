from flask import Blueprint, request, jsonify
from app.services.review_service import ReviewService

bp = Blueprint('reviews', __name__, url_prefix='/books/<int:book_id>/reviews')
review_service = ReviewService()

@bp.route('', methods=['POST'])
async def add_review(book_id):
    data = request.json
    review = await review_service.create_review(book_id, data)
    return jsonify(id=review.id), 201

@bp.route('', methods=['GET'])
async def list_reviews(book_id):
    reviews = await review_service.get_reviews_for_book(book_id)
    return jsonify([r.to_dict() for r in reviews])