from mysqlconnection import connectToMySQL
DATABASE = 'dojo_servey_schema'
from flask import flash


class Dojo:
    def __init__(self, data):
        self.id = ['id']
        self.location = data['location']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def insert(cls, data):
        query = """
        INSERT INTO dojos (name, location, comment)
        VALUES (%(name)s ,%(location)s, %(comment)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name']) < 1:
            flash('must input a name')
            is_valid = False
        return is_valid