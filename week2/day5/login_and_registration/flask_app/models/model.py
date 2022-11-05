
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')



class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']

    @classmethod
    def insert(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def get_by_email(cls, data):
        query = """
        SELECT * FROM users WHERE email = %(email)s
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM users WHERE id = %(id)s
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])


    @staticmethod
    def validate(user):
        is_valid = True
        if len(user['first_name']) < 1:
            flash('First name is required', 'reg')
            is_valid = False
        if len(user['last_name']) < 1:
            flash('Last name is required')
            is_valid = False
        if len(user['email']) < 1:
            flash('email is required')
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']):
            flash('invalid email', 'reg')
            is_valid = False
        else:
            data = {
                'email' : user['email']
            }
            potential_user = User.get_one(data)
            if potential_user:
                flash('email already taken', 'reg')
                is_valid = False
        if len(user['password']) < 7:
            flash('Password must be at least 8 characters long')
            is_valid = False
        elif user['password'] != user['confirm_pass']:
            flash('Passwords do not match', 'reg')
            is_valid = False
        return is_valid
