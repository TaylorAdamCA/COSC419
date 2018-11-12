from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myApp = Flask(__name__)

myApp.config.from_pyfile('../config.py')

db = SQLAlchemy(myApp)

