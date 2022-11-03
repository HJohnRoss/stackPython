from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


# CREATING THE NEW NINJA IN THE DATABASE
@app.route('/new_ninja/create', methods=['POST'])
def create_ninja():
    Ninja.insert(request.form)
    # REDIRECTING TO THE DOJO PAGE WHERE THE NEW NINJA IS LOCATED
    return redirect(f'/dojo/{request.form["dojo_id"]}/show')
  
  # RENDERING THE PAGE FOR CREATING A NINJA
@app.route('/new_ninja')
def new_ninja():
    # GETTING ALL THE INFO FROM THE DOJOS FROM THE MAIN PAGE
    one_dojo = Dojo.get_all()
    return render_template('new_ninja.html', one_dojo=one_dojo)
