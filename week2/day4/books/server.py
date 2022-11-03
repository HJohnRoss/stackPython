from flask_app.controllers import all_controller, author_controller, book_controller #  CHANGE THIS
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)