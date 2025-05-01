from flask import Blueprint, request, jsonify
from app.services.summary_service import SummaryService

bp = Blueprint('summaries', __name__)
summary_service = SummaryService()

@bp.route('/generate-summary', methods=['POST'])
async def generate():
    content = request.json.get("content")
    summary = await summary_service.generate_book_summary(content)
    return jsonify(summary=summary)