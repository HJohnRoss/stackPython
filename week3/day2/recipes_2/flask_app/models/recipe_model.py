from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
from flask_app.models import user_model
EMAIL_REGEX = re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under = data['under']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def one_to_many(cls):
        query = """
        SELECT * FROM recipes
        JOIN users ON recipes.user_id = users.id
        """
        result = connectToMySQL(DATABASE).query_db(query)
        recipe = []
        for row in result:
            recipes = cls(row)
            data = {
                **row,
                'id': row['users.id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            this_user = user_model.User(data)
            recipes.user = this_user
            recipe.append(recipes)
        return recipe

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO recipes (name, description, instructions, date_made, under, user_id)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under)s, %(user_id)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def update(cls, data):
        query = """
        UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s,
        date_made = %(date_made)s, under = %(under)s
        WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM recipes
        JOIN users ON recipes.user_id = users.id
        WHERE recipes.id = %(id)s
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        one_recipe = []
        for row in result:
            recipe = cls(row)
            data = {
                **row,
                'id': row['users.id'],
                'created_id': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            this_user = user_model.User(data)
            recipe.user = this_user
            one_recipe.append(recipe)
        return one_recipe

    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM recipes
        WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @staticmethod
    def validate(recipe):
        is_valid = True
        if len(recipe['name']) < 1:
            flash('name is required')
            is_valid = False
        elif len(recipe['name']) < 2:
            flash('name must be 3 characters')
            is_valid = False
        if len(recipe['description']) < 1:
            flash('description is required')
            is_valid = False
        elif len(recipe['description']) < 2:
            flash('description must be 3 characters')
            is_valid = False
        if len(recipe['instructions']) < 1:
            flash('instructions is required')
            is_valid = False
        elif len(recipe['instructions']) < 2:
            flash('instructions must be 3 characters')
            is_valid = False
        if 'under' not in recipe:
            is_valid = False
            flash('under 30 minutes is required')
        return is_valid
