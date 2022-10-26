from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/success")
def success():
    return "Success"


@app.route('/hello/<string:user>/<int:num>')
def hello(user, num):
    return render_template("hello.html", user=user, num=num)


if __name__ == "__main__":
    app.run(debug=True)
