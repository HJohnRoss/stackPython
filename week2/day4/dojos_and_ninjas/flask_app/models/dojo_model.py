from flask_app.config.mysqlconnection import connectToMySQL
from .ninja_model import Ninja
DATABASE = 'dojos_and_ninjas_db'


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # GET ALL METHOD
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in result:
            dojos.append(cls(dojo))
        return dojos
      
      
    # CREATING A NEW DOJO
    @classmethod
    def insert(cls, data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
      
      
    # GETTING A NINJA (JOIN)
    @classmethod
    def get_ninjas(cls, data):
        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        # THIS IS SENDING THE NINJA JOIN TO THE NINJAS CLASS TO RENDER IT
        dojo = cls(result[0])
        for row in result:
            ninjainfo = {
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'age' : row['age'],
                'created_at' : row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at'],
            }
            # 
            dojo.ninjas.append(Ninja(ninjainfo))
        return dojo