from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def main():
    return render_template("index.html")

@app.route("/result")
def showResult():
    return render_template("result.html", name1=request.args['name1'],
                           location=request.args['location'], message=request.args['message'],
                           language=request.args['language'])

if __name__ == "__main__":
    app.run(debug=True)
