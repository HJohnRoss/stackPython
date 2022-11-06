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
        self.user = None

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

    @classmethod
    def get_user_recipes(cls):
        query = """
        SELECT * FROM recipes
        JOIN users ON users.id = recipes.user_id 
        """
        result = connectToMySQL(DATABASE).query_db(query)
        if not result:
            return False
        recipe = []
        # recipes = cls(result)
        # ^ this is how u normally do it
        for row in result:
            recipes = cls(row)
            # ^ this combines the id and user_id cls(row)
            data = {
                **row,
                'id': row['users.id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            #     {
            #     'id': row['id'],
            #     'first_name': row['first_name'],
            #     'last_name': row['last_name'],
            #     'email': row['email'],
            #     'password': row['password'],
            #     'created_at': row['created_at'],
            #     'updated_at': row['updated_at']
            # }]
            this_user = user_model.User(data)
            recipes.user = this_user
            recipe.append(recipes)
            # recipes.user.append(User(data[1]))
            # user_recipe.append(recipe_model.Recipe(recipe_data))
            # user_recipe.append(User(user_data))
        return recipe

    @classmethod
    def get_one_recipe(cls, data):
        query = """
        SELECT * FROM recipes
        JOIN users ON users.id = recipes.user_id
        WHERE recipes.id = %(id)s 
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        recipe = []
        # recipes = cls(result)
        # ^ this is how u normally do it
        for row in result:
            recipes = cls(row)
            # ^ this combines the id and user_id cls(row)
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
    def delete_one(cls, data):
        query = """
        DELETE FROM recipes WHERE id = %(id)s
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def update_recipe(cls, data):
        query = """
        UPDATE recipes
        SET name = %(name)s, under = %(under)s, 
        instructions = %(instructions)s, description = %(description)s,
        date_made = %(date_made)s
        WHERE id = %(id)s
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    
    @staticmethod
    def validate(recipe):
        is_valid = True
        if len(recipe['name']) < 1:
            is_valid = False
            flash('name is required')
        elif len(recipe['name']) < 2:
            is_valid = False
            flash('name must be 3 characters')
        if len(recipe['description']) < 1:
            is_valid = False
            flash('description is required')
        elif len(recipe['description']) < 2:
            is_valid = False
            flash('description must be 3 characters')
        if len(recipe['instructions']) < 1:
            is_valid = False
            flash('instructions are required')
        elif len(recipe['instructions']) < 2:
            is_valid = False
            flash('instructions must be 3 characters')
        if len(recipe['date_made']) < 1:
            is_valid = False
            flash('date is required')
        if 'under' not in recipe:
            is_valid = False
            flash('under 30 minutes required')
        return is_valid