from flask import render_template, redirect, request, session
from flask_app import app

from flask_app.models import author_model # CHANGE THIS


@app.route('/author/create', methods=['POST'])
def create_author():
    author_model.Author.insert(request.form)
    redirect('/')