from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def main():
    return render_template("index.html")


@app.route("/result", methods=['POST'])
def showResult():
    session['name1'] = request.form['name1']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['message'] = request.form['message']
    return redirect('/show')


@app.route('/show')
def show():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
