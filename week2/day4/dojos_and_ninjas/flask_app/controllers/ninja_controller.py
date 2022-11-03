from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


@app.route('/new_ninja')
def new_ninja():
    one_dojo = Dojo.get_all()
    return render_template('new_ninja.html', one_dojo=one_dojo)
  
@app.route('/new_ninja/create', methods=['POST'])
def create_ninja():
    Ninja.insert(request.form)
    return redirect(f'/dojo/{request.form["dojo_id"]}/show')