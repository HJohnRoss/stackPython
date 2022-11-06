from flask_app.models import user_model, recipe_model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session
from flask_app import app
bcrypt = Bcrypt(app)


@app.route('/new_recipe/show')
def show_new_recipe():
    return render_template('create_recipe.html')


@app.route('/new_recipe/create', methods=['POST'])
def create_recipe():
    recipe_model.Recipe.insert_into(request.form)
    return redirect(f'/recipes/{session["user_id"]}/show_all')