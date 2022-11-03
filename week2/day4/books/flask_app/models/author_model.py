from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def insert(cls, data):
        query = """
        INSERT INTO authors (name)
        VALUES (%(name)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors"
        result = connectToMySQL(DATABASE).query_db(query)
        authors = []
        for author in result:
            authors.append(cls(author))
        return authors