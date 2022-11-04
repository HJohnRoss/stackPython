from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import model  # CHANGE THIS


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/submit/email')
def email_page():
    all_emails = model.Email.get_all()
    return render_template("emails.html", all_emails=all_emails)


@app.route('/create/email', methods=['POST'])
def create_email():
    if not model.Email.validation(request.form):
        return redirect('/')
    model.Email.insert(request.form)
    return redirect('/submit/email')