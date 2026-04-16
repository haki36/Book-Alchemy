from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    birth_date = Column(String(50), nullable=False)
    date_of_death = Column(String(50), nullable=True)

    books = relationship('Book', backref='author')

    def __repr__(self):
        return f"<Author {self.name}>"

    def __str__(self):
        return f"{self.name} (ID: {self.id})"

class Book(db.Model):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(String(20), unique=True, nullable=False)
    title = Column(String(200), nullable=False)
    publication_year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
