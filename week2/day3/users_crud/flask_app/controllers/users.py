from flask import render_template, redirect, request, session
from flask_app import app
# ...server.py
from flask_app.models.users import User


#  =============== MAIN ================
@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users=users)

# =============== NEW USER ================
@app.route('/new_user')
def new_user():
    return render_template('new_user.html')
  
@app.route('/insert_user', methods=['POST'])
def add():
    User.insert(request.form)
    return redirect('/')

# =============== GET ONE ================
@app.route('/show_user/<int:one_user>')
def show_user(one_user):
    data = {
      'id': one_user
    }
    return render_template('show_user.html', one_user=User.get_one(data))

# =============== EDIT USER ================
@app.route('/edit_user/<int:one_user>')
def edit_user(one_user):
    data = {
      'id' : one_user
    }
    return render_template('edit_user.html', one_user=User.get_one(data))

@app.route('/edit_user/success/<int:one_user>', methods=['POST'])
def user_success(one_user):
    data =  {
      **request.form, 'id' : one_user
    }
    User.update(data)
    return redirect('/')
  
# =============== DELETE ================
@app.route('/delete_user/<int:one_user>')
def delete(one_user):
    data = {
      'id' : one_user
    }
    User.delete(data)
    return redirect('/')