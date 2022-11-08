from flask_app.models import book_model, user_model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session
from flask_app import app
bcrypt = Bcrypt(app)


@app.route('/')
def main():
    return redirect('/authors/new')
