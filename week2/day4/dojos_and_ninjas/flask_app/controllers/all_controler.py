from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja


@app.route('/')
def main():
    ninjas = Ninja.get_all()
    dojos = Dojo.get_all()
    return render_template("index.html", ninjas=ninjas, dojos=dojos)


@app.route('/dojo/<int:id>/show')
def all_ninjas(id):
    data = {
        'id': id
    }
    return render_template('dojos.html', one_dojo=Dojo.get_ninjas(data))
