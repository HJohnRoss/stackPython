from flask import Flask
app = Flask(__name__)


@app.rout()
def error():
    return "error"


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/dojo')
def dojo():
    return "Dojo"


@app.route('/say/<user>')
def user(user):
    return f"Hi {user}"


@app.route('/repeat/<int:num>/<string:user>')
def repeat(num, user):
    return f"{user * num}"


if __name__ == "__main__":
    app.run(debug=True)
