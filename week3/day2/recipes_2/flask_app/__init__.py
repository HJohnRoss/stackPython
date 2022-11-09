from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"
DATABASE = "recipes_schema_2" # CHANGE THIS
