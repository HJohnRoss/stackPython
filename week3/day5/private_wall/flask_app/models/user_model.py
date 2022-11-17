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
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    

    @classmethod
    def select_some(cls, data):
        query = """
		SELECT * FROM users WHERE users.id 
        NOT IN (SELECT user_id from skeptics WHERE user_id = %(id)s)
        """
        users = []
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            for row in result:
                users.append(cls(row))
            return users
        return False
    
    @classmethod
    def get_by_email(cls, data):
        query = """
        SELECT * FROM users WHERE email = %(email)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return False

    @staticmethod
    def validate(user):
        is_valid = True
        if len(user['first_name']) < 1:
            flash('first name required', 'reg')
            is_valid = False
        elif len(user['first_name']) < 2:
            flash('first name must be 2 characters', 'reg')
            is_valid = False
        if len(user['last_name']) < 1:
            flash('last name required', 'reg')
            is_valid = False
        elif len(user['last_name']) < 2:
            flash('last name must be 2 characters', 'reg')
            is_valid = False
        if len(user['email']) < 1:
            flash('email is required', 'reg')
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']):
            flash('email is invalid', 'reg')
            is_valid = False
        else:
            data = {
                'email': user['email']
            }
            potential_user = User.get_by_email(data)
            if potential_user:
                flash('email taken', 'reg')
                is_valid = False
        if len(user['password']) < 7:
            flash('password must be 8 characters', 'reg')
            is_valid = False
        elif not user['password'] == user['confirm_pw']:
            is_valid = False
            flash('passwords dont match', 'reg')
        return is_valid
