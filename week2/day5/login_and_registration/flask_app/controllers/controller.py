from flask_app.models import model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session
from flask_app import app
bcrypt = Bcrypt(app)

# main routes


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    data = {
        'id': session['user_id']
    }
    logged_user = model.User.get_one(data)
    if 'user_id' not in session:
        return redirect('/')
    return render_template("logout.html", logged_user=logged_user)

# register


@app.route('/user/create', methods=['POST'])
def creat_user():
    if not model.User.validate(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    user_id = model.User.insert(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

# log in


@app.route('/login', methods=['POST'])
def login():
    data = {'email': request.form['email']}
    user_in_db = model.User.get_by_email(data)
    if not user_in_db:
        flash("invalid email", 'log')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('invalid password', 'log')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

# log out


@app.route('/user/logout')
def logout():
    del session['user_id']
    return redirect('/')
