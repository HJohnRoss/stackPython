from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)


# ================== GET ALL ==================
@app.route('/')
def add_user():
    return render_template("index.html")


@app.route('/users')
def users():
    users = User.get_all()
    return render_template("users.html", users=users)


# ====================== SAVE ==================
@app.route('/update/users', methods=['POST'])
def update_users():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.save(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
