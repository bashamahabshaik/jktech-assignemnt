import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql+asyncpg://admin:admin@db:5432/booksdb")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
