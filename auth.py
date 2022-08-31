from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить')
    submit = SubmitField('Войти')
