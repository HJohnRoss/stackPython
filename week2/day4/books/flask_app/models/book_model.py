from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        
    @classmethod
    def insert(cls, data):
        query = """
        INSERT INTO books (title, num_of_pages)
        VALUES (%(title)s, %(num_of_pages)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM books
        """
        result = connectToMySQL(DATABASE).query_db(query)
        all_books = []
        if result:
            for row in result:
                all_books.append(cls(row))
        return all_books