
from flask_app import app
from flask_app.config import mysqlconnection
from flask_app.controllers import controller



# step one:
#     pip3 install pipenv

# step two:
#     pipenv install flask

# step three:
#     pipenv install PyMySQL flask flask-bcrypt

# step four:

    # pipenv shell

    
if __name__=="__main__":
    app.run(debug=True, port=5004)