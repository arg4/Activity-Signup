# project/activity_signup/forms.py

from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Optional

activity_choices = [('soccer', 'Soccer'),
                     ('dodgeball', 'Dodgeball'),
                     ('programming', 'Programming')]

#TODO add more form validators as you learn to use them
class AddEmployeeForm(Form):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    email_address = StringField('Email Address:', validators=[DataRequired(), Email()])
    #activity = StringField('Activity:', validators=[DataRequired()])
    activity = SelectField('Activity:', choices=activity_choices )
    comments = TextAreaField('Comments:', validators=[Optional()])
