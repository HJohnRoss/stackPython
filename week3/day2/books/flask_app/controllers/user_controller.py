from flask_app.models import user_model, book_model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session
from flask_app import app
bcrypt = Bcrypt(app)

@app.route('/authors/new')
def show_users():
    all_users = user_model.User.get_all()
    return render_template('create_user.html', all_users=all_users)

@app.route('/user/create', methods=['POST'])
def create_user():
    user_model.User.save(request.form)
    return redirect('/authors/new')

@app.route('/authors/<int:id>')
def one_author(id):
    data = {
        'id' : id
    }
    all_books = book_model.Book.select_some(data)
    one_user = user_model.User.get_one_user(data)
    return render_template('favorite_user.html', one_user=one_user, all_books=all_books)


@app.route('/favorite/<int:user_id>/new', methods=['POST'])
def add_fav(user_id):
    data = {
        'user_id' : user_id,
        'book_id' : request.form['book_id']
    }
    user_model.User.insert_fav(data)
    return redirect(f'/authors/{data["user_id"]}')