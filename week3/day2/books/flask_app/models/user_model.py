from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import book_model, user_model
import re
EMAIL_REGEX = re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        
    
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM users
        """
        result = connectToMySQL(DATABASE).query_db(query)
        return result
    
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (name)
        VALUES (%(name)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def get_one_user(cls, data):
        query = """
        SELECT * FROM users
        LEFT JOIN favorites ON users.id = favorites.user_id
        LEFT JOIN books ON books.id = favorites.book_id
        WHERE users.id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        books = []
        one_user = cls(result[0])
        for row in result:
            one_book = {
                **row,
                'id' : row['books.id'],
                'created_at' : row['books.created_at'],
                'updated_at' : row['books.updated_at']
            }
            this_book = book_model.Book(one_book)
            books.append(this_book)
        one_user.favs = books
        return one_user
    
    
    @classmethod
    def insert_fav(cls, data):
        query = """
        INSERT INTO favorites (user_id, book_id)
        VALUES (%(user_id)s, %(book_id)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def select_some(cls, data):
        query = """
        SELECT * FROM users WHERE users.id
        NOT IN (SELECT user_id from favorites WHERE book_id = %(id)s)
        """
        users = []
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            for row in result:
                users.append(cls(row))
            return users
        return []