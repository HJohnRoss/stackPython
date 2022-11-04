from dojo_model import Dojo
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def main():
    return render_template("index.html")


@app.route("/result", methods=['POST'])
def showResult():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show', form_info=Dojo.insert())


@app.route('/show')
def show():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
