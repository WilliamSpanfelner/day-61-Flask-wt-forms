from flask_wtf import FlaskForm
# [Handling Forms in Flask with Flask-WTF](https://hackersandslackers.com/flask-wtforms-forms/)
# The following command will install FlaskForm - the Flask specific equivalent of wtforms:
# pip3 install flask flask-wtf
# just open terminal and run from project directory.
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
"""
    Install email_validator with the following command:
    pip3 install email_validator 
"""


class LoginForm(FlaskForm):
    # Add validators
    email = StringField(label="Email",
                        validators=[
                            Email('Enter a valid email address'),
                            DataRequired()]
                        )
    password = PasswordField(label="Password",
                             validators=[
                                 Length(8),
                                 DataRequired()]
                             )
    submit = SubmitField(label='Log In')
