from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import Ninja
from flask_app import DATABASE


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
        for data in result:
            ninjainfo = {
                'id' : data['ninjas.id'],
                'first_name' : data['first_name'],
                'last_name' : data['last_name'],
                'age' : data['age'],
                'created_at' : data['ninjas.created_at'],
                'updated_at' : data['ninjas.updated_at'],
            }
            # PUSHING INTO NINJAS
            dojo.ninjas.append(Ninja(ninjainfo))
        return dojo