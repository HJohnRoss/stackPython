from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import ninja_model
from flask_app.models import dojo_model


# CREATING THE NEW NINJA IN THE DATABASE
@app.route('/new_ninja/create', methods=['POST'])
def create_ninja():
    ninja_model.Ninja.insert(request.form)
    # REDIRECTING TO THE DOJO PAGE WHERE THE NEW NINJA IS LOCATED
    return redirect(f'/dojo/{request.form["dojo_id"]}/show')
  
  # RENDERING THE PAGE FOR CREATING A NINJA
@app.route('/new_ninja')
def new_ninja():
    # GETTING ALL THE INFO FROM THE DOJOS FROM THE MAIN PAGE
    one_dojo = dojo_model.Dojo.get_all()
    return render_template('new_ninja.html', one_dojo=one_dojo)
