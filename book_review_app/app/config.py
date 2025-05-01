import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("htpp://localhost:5432", "postgresql+asyncpg://admin:admin@localhost/booksdb")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
