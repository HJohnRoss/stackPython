from flask_app.models import user_model, recipe_model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session
from flask_app import app
bcrypt = Bcrypt(app)


@app.route('/')
def main():
    if 'user_id' in session:
        return redirect(f'/recipes/{session["user_id"]}/show_all')
    return render_template("login.html")


@app.route('/recipes/<int:id>/show_all')
def all_recipes(id):
    if not 'user_id' in session:
        return redirect('/')
    return render_template('all_recipes.html', users=user_model.User.get_user_recipes())


@app.route('/back_home')
def home():
    return redirect(f'/recipes/{session["user_id"]}/show_all')
