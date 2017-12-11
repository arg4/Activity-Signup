# Activity Signup Application
Simple Flask application that adds an employee to a list along with their chosen activity

## Instructions
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
