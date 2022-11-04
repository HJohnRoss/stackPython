from flask import render_template, redirect, request, session
from flask_app import app

from flask_app.models import author_model, book_model # CHANGE THIS


@app.route('/')
def main():
    authors = author_model.Author.get_all()
    return render_template("create_author.html", authors=authors)

@app.route('/books/favorites/<int:id>')
def book_fav_by(id):
    data = {
        'id' : id
    }
    all_authors = author_model.Author.get_all()
    return render_template("show_book.html", one_book = book_model.Book.get_one(data), all_authors=all_authors)