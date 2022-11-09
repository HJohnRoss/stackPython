from flask_app.models import user_model, recipe_model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session
from flask_app import app
bcrypt = Bcrypt(app)


@app.route('/dashboard')
def dashboard_show():
    if 'user_id' not in session:
        return redirect('/')
    recipes = recipe_model.Recipe.one_to_many()
    return render_template('dashboard.html', recipes=recipes)

@app.route('/recipe/create')
def create_recipe_show():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('create_recipe.html')

@app.route('/recipes/create_recipe', methods=['POST'])
def add_recipe():
    if not recipe_model.Recipe.validate(request.form):
        return redirect('/recipe/create')
    recipe_model.Recipe.save(request.form)
    return redirect('/dashboard')


@app.route('/recipe/edit/<int:id>')
def edit_recipe(id):
    data = {
        'id' : id
    }
    if 'user_id' not in session:
        return redirect('/')
    one_recipe=recipe_model.Recipe.get_one(data)
    return render_template('edit_recipe.html', one_recipe=one_recipe)


@app.route('/recipes/update/<int:id>', methods=['POST'])
def update_recipe(id):
    data = {
        **request.form,
        'id' : id
    }
    if not recipe_model.Recipe.validate(request.form):
        return redirect(f'/recipe/edit/{id}')
    recipe_model.Recipe.update(data)
    return redirect('/dashboard')


@app.route('/recipe/delete/<int:id>')
def delete(id):
    data = {
        'id' : id
    }
    recipe_model.Recipe.delete(data)
    return redirect('/dashboard')

@app.route('/recipe/show/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : id
    }
    one_recipe = recipe_model.Recipe.get_one(data)
    return render_template('show_recipe.html', one_recipe=one_recipe)