from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo_model import Dojo

# CREATING A NEW DOJO ON THE MAIN PAGE
@app.route('/dojo/create_dojo', methods=['POST'])
def create_dojo():
    Dojo.insert(request.form)
    return redirect('/')