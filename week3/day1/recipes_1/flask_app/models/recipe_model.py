from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
import re
EMAIL_REGEX = re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under = data['under']
        self.instructions = data['instructions']
        self.description = data['description']
        self.date_made = data['date_made']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM recipes;
        """
        result = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for recipe in result:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def insert_into(cls, data):
        query = """
        INSERT INTO recipes (name, under, instructions, description, date_made, user_id)
        VALUES (%(name)s, %(under)s, %(instructions)s, %(description)s,
        %(date_made)s, %(user_id)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
