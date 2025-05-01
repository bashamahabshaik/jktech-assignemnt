import asyncio
from app.config import Config
from sqlalchemy.ext.asyncio import create_async_engine
from app.models.book import Book
from app.models.review import Review
from app.models import Base 

async def init_db():
    engine = create_async_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("Database schema created.")

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(init_db())
