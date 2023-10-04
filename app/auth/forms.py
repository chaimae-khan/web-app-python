# INCREMENTAL CODE FOR SECTION : 11 LECTURE : 44 - VALIDATING FORMS
# auth/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField ,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class RegistrationForm(FlaskForm):
    first_name = StringField('first Name', validators=[DataRequired(), Length(3,15, message='between 3 to 15 characters')])
    last_name = StringField('last Name', validators=[DataRequired(), Length(3,15, message='between 3 to 15 characters')])
    job_title = StringField('job title', validators=[DataRequired(), Length(3,15, message='between 3 to 15 characters')])
    is_admin = BooleanField('Is Admin')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='password must match')])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('Stay logged-in')
    submit = SubmitField('LogIn')
