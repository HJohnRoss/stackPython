from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
import re
EMAIL_REGEX = re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM books
        """
        result = connectToMySQL(DATABASE).query_db(query)
        return result
    
    @classmethod
    def select_some(cls, data):
        query = """
        SELECT * FROM books WHERE books.id 
        NOT IN (SELECT book_id from favorites WHERE user_id = %(id)s)
        """
        books = []
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            for row in result:
                books.append(cls(row))
            return books
        return []
    
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO books (title, num_of_pages)
        VALUES (%(title)s, %(num_of_pages)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def get_one_book(cls, data):
        query = """
        SELECT * FROM books
        LEFT JOIN favorites ON books.id = favorites.book_id
        LEFT JOIN users ON users.id = favorites.user_id
        WHERE books.id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        users = []
        one_book = cls(result[0])
        for row in result:
            one_user = {
                **row,
                'updated_at' : row['updated_at'],
                'created_at' : row['created_at']
            }
            this_user = user_model.User(one_user)
            users.append(this_user)
        one_book.favs = users
        return one_book