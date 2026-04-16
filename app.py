from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

db.init_app(app)

# Only for creating tables once
# with app.app_context():
#     db.create_all()

@app.route('/add_author', methods = ['GET', 'POST'])
def add_author():
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


@app.route('/add_book', methods = ['GET', 'POST'])
def add_book():
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

@app.route('/', methods = ['GET', 'POST'])
def home():
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
