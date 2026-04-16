"""
Flask application for a simple digital library.

This application allows users to:
- add authors to the database
- add books to the database
- view all books on the home page
- sort books by title or author
- search for books by title

The application uses Flask-SQLAlchemy with a SQLite database.
"""

import os
from flask import Flask, render_template, request
from data_models import db, Author, Book

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

db.init_app(app)

# Only for creating tables once
# with app.app_context():
#     db.create_all()

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    """
    Display the add author form and handle author creation.
    GET:
        Render the form for adding a new author.
    POST:
        Create a new Author object from form data,
        save it to the database, and display a success message.
    Returns:
        str: Rendered HTML page for adding an author.
    """
    success_message = None

    if request.method == 'POST':
        add_new_author = Author(
            name = request.form.get('name'),
            birth_date = request.form.get('birth_date'),
            date_of_death = request.form.get('date_of_death')
        )
        db.session.add(add_new_author)
        db.session.commit()
        success_message = 'Author was added successfully.'

    return render_template('add_author.html', success_message=success_message)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    """
    Display the add book form and handle book creation.
    GET:
        Render the form for adding a new book.
        Also load all authors so the user can choose one from a dropdown.
    POST:
        Create a new Book object from form data,
        save it to the database, and display a success message.
    Returns:
        str: Rendered HTML page for adding a book.
    """
    success_message = None
    authors = Author.query.all()

    if request.method == 'POST':
        add_new_book = Book(
            title = request.form.get('title'),
            isbn = request.form.get('isbn'),
            publication_year = request.form.get('publication_year'),
            author_id = request.form.get('author_id')
        )
        db.session.add(add_new_book)
        db.session.commit()
        success_message = 'Book was added successfully.'

    return render_template('add_book.html', authors=authors, success_message=success_message)

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Display the home page with all books, sorting, and search functionality.
    The route:
    - reads the selected sorting option from the query string
    - reads the search term from the query string
    - filters books by title if a search term is provided
    - sorts books by title or author name
    Returns:
        str: Rendered HTML page showing the book list.
    """
    sort_data = request.args.get('sort', 'title')
    search_term = request.args.get('search', '')

    books_query = Book.query

    if search_term:
        books_query = books_query.filter(Book.title.ilike(f'%{search_term}%'))

    books = books_query.all()

    if sort_data == 'title':
        books = sorted(books, key=lambda book: book.title.lower())
    elif sort_data == 'author':
        books = sorted(books, key=lambda book: book.author.name.lower())

    return render_template(
        'home.html',
        books=books,
        sort_data=sort_data,
        search_term=search_term
    )

if __name__ == "__main__":
    app.run(debug=True)
