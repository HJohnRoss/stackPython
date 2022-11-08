from flask_app.models import friendship_model, user_model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session
from flask_app import app
bcrypt = Bcrypt(app)


@app.route('/')
def main():
    all_users = user_model.User.get_all()
    friendships = friendship_model.Friendships.show_friends()
    return render_template("index.html", all_users=all_users, friendships=friendships)


@app.route('/user/create', methods=['POST'])
def create():
    user_model.User.save(request.form)
    return redirect('/')


@app.route('/friendship/create', methods=['POST'])
def friend_add():
    friendship_model.Friendships.add_friend(request.form)
    return redirect('/')