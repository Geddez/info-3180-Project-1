from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config Values
# USERNAME = 'admin'
# PASSWORD = 'password123'
# HOST = 'localhost'
UPLOAD_FOLDER = './app/static/uploads'
SECRET_KEY = 'Justkey'
# DATABASE_NAME = 'project1'
# SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}/{3}' \
#                             .format(USERNAME, PASSWORD,
#                                     HOST, DATABASE_NAME)
DATABASE_URL=''

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)

from app import views, models
