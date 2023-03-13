from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('login', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Enter')
