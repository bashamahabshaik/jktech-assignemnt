from app.utils.llama3_client import Llama3Client

class SummaryService:
    def __init__(self):
        self.client = Llama3Client()

    async def generate_book_summary(self, content):
        return await self.client.generate_summary(content)