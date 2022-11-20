from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

# Создаем класс, чтобы отслеживать все строки, которые нам написал пользователь
class LoginForm(FlaskForm):
    # Создаем строку, которая будет показывать пользователю, что мы здесь вводим Имя
    # validators=[Required()] позволяет отслеживать, что написал пользователь
    # Базовые валидаторы
    # DataRequired() проверяет ввел ли пользователь какую-то ифнормацию в поле, является ли 
    # строка пустой
    # Email() проверяет является ли введенный email адрес действующим
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Почта', validators=[Email()])
    #SubmitField позволяет отслеживать нажатие 
    submit = SubmitField('Submit')
    