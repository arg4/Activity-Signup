# Activity Signup Application
Simple Flask application that adds an employee to a list along with their chosen activity

## Instructions
This application was build using flask, you should use a virtual environment to run it, after installing all the packages in `requirements.txt` with pip and updating the values in `instance/flask.cfg` run the application in the root directory with `python run.py`.


Replace values in `instance/flask.cfg` with relevant values
```python
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)
SECRET_KEY = b'<secret key>'
DEBUG = True

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@<dbname>'
SQLALCHEMY_TRACK_MODIFICATIONS = True (activity_env) r3d@c4rdinal:~/Programming/activities_app/activity_proj$ 
```

The employee can choose their own activity if in `project/activity_signup/forms.py` you comment
```python
activity = SelectField('Activity:', choices=activity_choices )
```
and uncomment 
```python
activity = StringField('Activity:', validators=[DataRequired()])
```
You can also add and remove 'activity choices' in this file.
