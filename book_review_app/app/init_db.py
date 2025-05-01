# app/init_db.py

import asyncio
from app.config import Config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app.models.book import Book
from app.models.review import Review
import random
from faker import Faker

fake = Faker()

async def seed_data(session: AsyncSession):
    books = [
        Book(
            title=fake.sentence(nb_words=4),
            author=fake.name(),
            genre=fake.word(),
            year_published=random.randint(1950, 2024),
            summary=fake.text(max_nb_chars=200)
        ) for _ in range(25)
    ]
    session.add_all(books)
    await session.flush()  # to populate book IDs

    reviews = [
        Review(
            book_id=random.choice(books).id,
            user_id=fake.uuid4(),
            review_text=fake.text(max_nb_chars=100),
            rating=random.randint(1, 5)
        ) for _ in range(100)
    ]
    session.add_all(reviews)
    await session.commit()

async def init_db():
    engine = create_async_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("Database schema created.")

    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        await seed_data(session)

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(init_db())
