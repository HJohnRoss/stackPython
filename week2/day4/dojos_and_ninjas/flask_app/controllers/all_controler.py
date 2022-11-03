from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask_app.models import ninja_model 

# RENDERING THE MAIN PAGE
@app.route('/')
def main():
    ninjas = ninja_model.Ninja.get_all()
    dojos = Dojo.get_all()
    return render_template("index.html", ninjas=ninjas, dojos=dojos)

# SHOWING THE DOJOS + THE NINJAS IN SAID DOJO
@app.route('/dojo/<int:id>/show')
def all_ninjas(id):
    data = {
        'id': id
    }
    return render_template('dojos.html', one_dojo=Dojo.get_ninjas(data))

