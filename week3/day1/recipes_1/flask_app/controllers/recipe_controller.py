from flask_app.models import user_model, recipe_model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session
from flask_app import app
bcrypt = Bcrypt(app)


@app.route('/new_recipe/show')
def show_new_recipe():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('create_recipe.html')


@app.route('/new_recipe/create', methods=['POST'])
def create_recipe():
    if not recipe_model.Recipe.validate(request.form):
        return redirect("/new_recipe/show")
    recipe_model.Recipe.insert_into(request.form)
    return redirect(f'/recipes/{session["user_id"]}/show_all')


@app.route('/recipes/<int:id>/show')
def show_one(id):
    if not 'user_id' in session:
        return redirect('/')
    data = {
        'id': id
    }
    one_recipe = recipe_model.Recipe.get_one_recipe(data)
    return render_template('one_recipe.html', one_recipe=one_recipe)


@app.route('/recipes/<int:id>/delete')
def delete(id):
    data = {
        'id': id
    }
    recipe_model.Recipe.delete_one(data)
    return redirect(f'/recipes/{session["user_id"]}/show_all')


@app.route('/recipes/<int:id>/edit')
def edit(id):
    if not 'user_id' in session:
        return redirect('/')
    data = {
        'id': id
    }
    one_recipe = recipe_model.Recipe.get_one_recipe(data)
    return render_template('edit_recipe.html', one_recipe=one_recipe)


@app.route('/new_recipe/edit/success', methods=['POST'])
def update_recipe():
    if not recipe_model.Recipe.validate(request.form):
        return redirect(f"/recipes/{request.form['id']}/edit")
    recipe_model.Recipe.update_recipe(request.form)
    return redirect('/back_home')
