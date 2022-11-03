from flask import render_template, redirect, request, session
from flask_app import app

from flask_app.models import book_model # CHANGE THIS


@app.route('/books')
def show_books():
    all_books = book_model.Book.get_all()
    return render_template('create_books.html', all_books=all_books)

@app.route('/books/create', methods=['POST'])
def create_book():
    book_model.Book.insert(request.form)
    return redirect('/books')