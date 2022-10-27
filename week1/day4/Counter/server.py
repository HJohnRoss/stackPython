from contextlib import redirect_stderr
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def showNum():
    if "num" in session:
        session['num'] += 1
    else:
        session['num'] = 1
    return render_template("index.html", num_of_visits=session['num'])

@app.route('/add')
def addVisit():
    session['num'] += 1
    return redirect('/')

@app.route('/destroy')
def destrySes():
    session['num'] = 0
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
