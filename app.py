from resources.routes import initialize_routes
import json

from flask import Flask, Response, jsonify, request
from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_restful import Api

from database.db import initialize_db
from resources.errors import errors
# from resources.routes import initialize_routes

app = Flask(__name__)
# app.config.from_envvar('ENV_FILE_LOCATION')
# mail = Mail(app)

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
# jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/flask_restapi_user_signup_create'
}
initialize_db(app)
# app.register_blueprint(movies)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=False)
