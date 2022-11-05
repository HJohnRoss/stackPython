from flask_app.models import user_model, recipe_model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session
from flask_app import app
bcrypt = Bcrypt(app)


@app.route('/register/user', methods=['POST'])
def register_user():
    if not user_model.User.user_validation(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    user_id = user_model.User.create_user(data)
    session['user_id'] = user_id
    return redirect('/recipes/show_all')

@app.route('/login/user', methods=['POST'])
def login_user():
    data = {'email' : request.form['email']}
    user_in_db = user_model.User.get_by_user(data)
    if not user_in_db:
        flash('Invalid email/password', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid email/password', 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/recipes/show_all')

@app.route('/logout')
def logout():
    del session['user_id']
    return redirect('/')