from flask_app.config.mysqlconnection import ConectToMySQL


class Class:
    def __init__(self, data):
        self.id = data['id']