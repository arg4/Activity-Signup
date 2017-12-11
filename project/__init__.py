# IMPORTS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)

# Blueprints
from project.activity_signup.views import activity_blueprint

# Register Blueprint
app.register_blueprint(activity_blueprint)
