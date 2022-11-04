from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.emails = data['emails']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM emails
        """
        result = connectToMySQL(DATABASE).query_db(query)
        emails = []
        for one_email in result:
            emails.append(cls(one_email))
        return emails
    
    @classmethod
    def insert(cls, data):
        query = """
        INSERT INTO emails (emails)
        VALUES (%(emails)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @staticmethod
    def validation(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['emails']): 
            flash("Invalid email address!")
            is_valid = False
        else:
            flash("email successfully entered")
        return is_valid