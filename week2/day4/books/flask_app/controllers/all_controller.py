from flask import render_template, redirect, request, session
from flask_app import app

from flask_app.models import author_model, book_model # CHANGE THIS


@app.route('/')
def main():
    authors = author_model.Author.get_all()
    return render_template("create_author.html", authors=authors)