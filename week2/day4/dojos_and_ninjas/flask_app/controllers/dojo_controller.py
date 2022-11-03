from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import dojo_model

# CREATING A NEW DOJO ON THE MAIN PAGE
@app.route('/dojo/create_dojo', methods=['POST'])
def create_dojo():
    dojo_model.Dojo.insert(request.form)
    return redirect('/')