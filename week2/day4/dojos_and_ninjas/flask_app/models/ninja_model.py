from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age'] # why do i need to take out the forein key here
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # GET ALL NINJAS
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    # INSERT INTO NINJAS
    @classmethod
    def insert(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
