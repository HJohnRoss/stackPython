from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author_model
from flask_app import DATABASE


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.authors_favorited = []
        
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
    
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM books
        LEFT JOIN favorites ON favorites.book_id = books.id
        LEFT JOIN authors ON authors.id = favorites.author_id
        WHERE books.id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        book = (cls(result[0]))
        row = result[0]
        for row in result:
            author_info = {
                 **row,
                 'id' : row['authors.id'],
                 'created_at' : row['authors.created_at'],
                 'updated_at' : row['authors.updated_at']
            }
            this_author = author_model.Author(author_info)
            book.authors_favorited.append(this_author)
            
            # book.authors_favorited.append(author_model.Author(author_info))
        return book