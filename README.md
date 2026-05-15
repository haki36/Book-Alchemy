# 📚 Digital Library App (Flask + SQLite + SQLAlchemy)

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-black)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Bootcamp](https://img.shields.io/badge/Masterschool-Bootcamp-orange)

> A **Flask web application** for managing a small digital library with
> authors, books, search, sorting, cover images, and delete functionality
> using **Flask-SQLAlchemy** and a **SQLite database**.

------------------------------------------------------------------------

# 📌 Overview

This project demonstrates how to:

- Build a Flask web application
- Connect Flask with a SQLite database
- Use Flask-SQLAlchemy as an ORM
- Create database models with relationships
- Add authors to the database
- Add books and connect them to authors
- Display all books on the home page
- Search books by title
- Sort books by title or author
- Delete books from the library
- Improve the user interface with CSS

------------------------------------------------------------------------

# 🖥️ Demo Flow

1. Start the Flask application
2. Open the web app in the browser
3. Add authors
4. Add books and assign them to authors
5. View all books on the home page
6. Search and sort books
7. Delete books from the library

Run:

```bash
flask run --host=0.0.0.0 --port=5002
```

Alternative:

```bash
python app.py
```

Open in browser:

```text
http://localhost:5002
```

------------------------------------------------------------------------

# ✨ Core Features

- Add authors
- Add books
- Store data in SQLite
- Use SQLAlchemy models
- Connect books with authors using a foreign key
- Display books on the home page
- Display author names for each book
- Display book covers using ISBN
- Search books by title
- Sort books by title
- Sort books by author name
- Delete books
- Show success messages after actions
- Simple responsive UI styling

------------------------------------------------------------------------

# 📂 Project Structure

```text
Digital-Library/
│
├── app.py
├── data_models.py
├── README.md
│
├── data/
│   └── library.sqlite
│
├── static/
│   └── style.css
│
└── templates/
    ├── home.html
    ├── add_author.html
    └── add_book.html
```

------------------------------------------------------------------------

# 🚀 Installation & Usage

## Requirements

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- Jinja2

Install dependencies:

```bash
pip install flask sqlalchemy flask_sqlalchemy jinja2
```

------------------------------------------------------------------------

## Database Setup

Create the SQLite database file inside the `data/` folder:

```bash
mkdir -p data
touch data/library.sqlite
```

Create the database tables once by temporarily enabling this block in `app.py`:

```python
with app.app_context():
    db.create_all()
```

After running the app once, comment it out again:

```python
# with app.app_context():
#     db.create_all()
```

------------------------------------------------------------------------

## Run the App

For Codio submission:

```bash
flask run --host=0.0.0.0 --port=5002
```

If Flask does not detect the app automatically:

```bash
flask --app app run --host=0.0.0.0 --port=5002
```

Local alternative:

```bash
python app.py
```

------------------------------------------------------------------------

# 🔗 Application Routes

| Method | Route                         | Description                         |
|--------|-------------------------------|-------------------------------------|
| GET    | `/`                           | Show all books                      |
| GET    | `/?search=<term>`             | Search books by title               |
| GET    | `/?sort=title`                | Sort books by title                 |
| GET    | `/?sort=author`               | Sort books by author name           |
| GET    | `/add_author`                 | Show add author form                |
| POST   | `/add_author`                 | Save a new author                   |
| GET    | `/add_book`                   | Show add book form                  |
| POST   | `/add_book`                   | Save a new book                     |
| POST   | `/book/<book_id>/delete`      | Delete a book from the database     |

------------------------------------------------------------------------

# 🧠 Technical Concepts Applied

- Flask application setup
- Flask routing
- HTML rendering with Jinja2 templates
- Handling GET and POST requests
- Form handling with `request.form`
- Query parameters with `request.args`
- Redirects with `redirect()` and `url_for()`
- Flash messages with `flash()`
- SQLite database connection
- Flask-SQLAlchemy configuration
- SQLAlchemy models
- Primary keys
- Foreign keys
- One-to-many relationship between authors and books
- Database insert and delete operations
- Search with `ilike()`
- Sorting with Python `sorted()`
- Dynamic cover image loading via ISBN

------------------------------------------------------------------------

# 🗄️ Database Models

## Author

The `Author` model stores author information.

Fields:

- `id`
- `name`
- `birth_date`
- `date_of_death`

## Book

The `Book` model stores book information.

Fields:

- `id`
- `isbn`
- `title`
- `publication_year`
- `author_id`

Relationship:

- One author can have many books
- Each book belongs to one author

------------------------------------------------------------------------

# 🔐 Error Handling

The application handles:

- Missing books with `get_or_404()`
- Empty search results
- Missing database tables after setup
- Redirecting after successful form submissions
- Flash messages after delete actions

------------------------------------------------------------------------

# 🎓 Learning Objectives

- Understand how Flask applications are structured
- Learn how to connect Flask with a database
- Understand SQLAlchemy models and relationships
- Practice CRUD-like functionality
- Work with forms and templates
- Use database queries for search and sorting
- Build a small full-stack web application
- Prepare a project for GitHub and portfolio presentation

------------------------------------------------------------------------

# 📈 Portfolio Upgrade Ideas

- Add book detail pages
- Add author detail pages
- Add author delete functionality
- Add book ratings from 1 to 10
- Add categories or genres
- Add user authentication
- Add pagination
- Add edit functionality for books and authors
- Replace SQLite with PostgreSQL
- Add Docker support
- Deploy the app to a cloud server
- Add AI-based book recommendations
- Improve the UI with Bootstrap or Tailwind CSS

------------------------------------------------------------------------

# 🇩🇪 Kurzbeschreibung

Eine einfache digitale Bibliothek mit Flask, SQLite und SQLAlchemy.

Die Anwendung ermöglicht das Hinzufügen von Autoren und Büchern,
zeigt alle Bücher auf der Startseite an und unterstützt Suche,
Sortierung, Cover-Anzeige und das Löschen von Büchern.

Dieses Projekt wurde im Rahmen des Masterschool Bootcamps erstellt
und dient als Übungsprojekt für Flask, Datenbanken und Webentwicklung.

------------------------------------------------------------------------

# 📄 License

MIT License

------------------------------------------------------------------------

# 👤 Author

Hakan Yildirim  
Python Software Developer (AI Track)  
Masterschool Bootcamp

GitHub: https://github.com/haki36  
LinkedIn: https://linkedin.com/in/hakan-yildirim-tech
