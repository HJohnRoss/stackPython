from flask import render_template, redirect, request, session
from flask_app import app

from flask_app.models.Classes import Class # CHANGE THIS


@app.route('/')
def main():
    return render_template("index.html")