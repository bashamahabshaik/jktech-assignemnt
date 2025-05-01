import httpx

class Llama3Client:
    def __init__(self, url="http://localhost:11434/api/generate"):
        self.url = url
        
    async def generate_summary(self, content: str) -> str:
        payload = {
            "model": "llama3.1:8b",
            "prompt": f"You are a helpful assistant. Read the following passage and write a short summary, even if the input is brief or incomplete. Be imaginative if needed and summarize in 1-2 lines:\n\n{content}",
            "stream": False
        }
        print(content,"////////////")
        async with httpx.AsyncClient() as client:
            response = await client.post(self.url, json=payload)
            data = response.json()
            return data["response"]
    
    async def generate_recommendations(self, preferences: dict, book_list: list[str]) -> str:
        prompt = f"""
            You are a helpful book recommendation assistant.

            User preferences:
            {preferences}

            Available books:
            {book_list}

            Please recommend best books that best match the user's preferences.
            Return only book titles with a short reason for each.
            """

        async with httpx.AsyncClient() as client:
            response = await client.post(self.url,
                json={
                    "model": "llama3.1:8b",
                    "prompt": prompt.strip(),
                    "stream": False
                }
            )

            response.raise_for_status()
            return response.json()["response"]