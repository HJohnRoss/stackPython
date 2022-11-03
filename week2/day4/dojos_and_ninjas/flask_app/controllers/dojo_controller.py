from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo_model import Dojo


@app.route('/dojo/create_dojo', methods=['POST'])
def create_dojo():
    Dojo.insert(request.form)
    return redirect('/')