from flask_app.models import user_model, book_model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session
from flask_app import app
bcrypt = Bcrypt(app)



@app.route('/book/show')
def book_home():
    all_books = book_model.Book.get_all()
    return render_template('create_book.html', all_books=all_books)

@app.route('/book/create', methods=['POST'])
def create_book():
    book_model.Book.save(request.form)
    return redirect('/book/show')

@app.route('/book/<int:id>')
def show_book(id):
    data = {
        'id' : id
    }
    all_users = book_model.Book.get_one_book(data)
    some_users = user_model.User.select_some(data)
    return render_template('favorite_book.html', all_users=all_users, some_users=some_users)

@app.route('/book/<int:book_id>/new', methods=['POST'])
def add_fav_book(book_id):
    data = {
        'book_id' : book_id,
        'user_id' : request.form['user_id']
    }
    user_model.User.insert_fav(data)
    return redirect(f'/book/{data["book_id"]}')