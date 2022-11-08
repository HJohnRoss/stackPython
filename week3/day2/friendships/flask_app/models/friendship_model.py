from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')


class Friendships:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_friend(cls, data):
        query = """
        INSERT INTO friendships (user_id, friend_id)
        VALUES (%(user_id)s, %(friend_id)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def show_friends(cls):
        query = """
        SELECT * FROM users
        LEFT JOIN friendships ON users.id = friendships.user_id
        JOIN users as user2 ON user2.id = friendships.friend_id;
        """
        result = connectToMySQL(DATABASE).query_db(query)
        return result
