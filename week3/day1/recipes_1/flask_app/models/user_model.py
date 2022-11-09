from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import recipe_model
import re
EMAIL_REGEX = re.compile(r'[^@ \t\r\n]+@[^z@ \t\r\n]+\.[^@ \t\r\n]+')


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipe = []
        self.user = None

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM users;
        """
        result = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in result:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM users
        WHERE users.id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # create user
    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # get by email
    @classmethod
    def get_by_user(cls, data):
        query = """
        SELECT * FROM users WHERE email = %(email)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        if len(result) < 1:
            return False
        return cls(result[0])

    # get one user
    # @classmethod
    # def get_user_recipes(cls):
    #     query = """
    #     SELECT * FROM recipes
    #     JOIN users ON users.id = recipes.user_id 
    #     """
    #     result = connectToMySQL(DATABASE).query_db(query)
    #     if not result:
    #         return False
    #     recipes = cls(result[0])
    #     for row in result:
            # data = [{
            #     **row,
            #     'id' : row['users.id'],
            #     'created_at' : row['created_at']
            # },
            #     {
            #     'id': row['id'],
            #     'first_name': row['first_name'],
            #     'last_name': row['last_name'],
            #     'email': row['email'],
            #     'password': row['password'],
            #     'created_at': row['created_at'],
            #     'updated_at': row['updated_at']
            # }]
    #         this_user = recipe_model.Recipe(data)
    #         recipes.user = this_user
    #         recipes.recipe.append(recipes)
    #         # recipes.user.append(User(data[1]))
    #         # user_recipe.append(recipe_model.Recipe(recipe_data))
    #         # user_recipe.append(User(user_data))
    #     return recipes.recipe

    # user validation
    @staticmethod
    def user_validation(user):
        is_valid = True
        if len(user['first_name']) < 1:
            flash('First name is required', 'reg')
            is_valid = False
        if len(user['last_name']) < 1:
            flash('Last name is required', 'reg')
            is_valid = False
        if len(user['email']) < 1:
            flash('Email is required', 'reg')
        elif not EMAIL_REGEX.match(user['email']):
            flash('Email invalid', 'reg')
            is_valid = False
        else:
            data = {
                'email': user['email']
            }
            potential_user = User.get_by_user(data)
            if potential_user:
                flash('Email already taken', 'reg')
                is_valid = False
        if len(user['password']) < 7:
            flash('Password must be 8 characters', 'reg')
            is_valid = False
        elif not user['password'] == user['confirm_pass']:
            flash("Password's do not match", 'reg')
            is_valid = False
        return is_valid
