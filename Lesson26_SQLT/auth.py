from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

# Создаем класс, чтобы отслеживать все строки, которые нам написал пользователь
class LoginForm(FlaskForm):
    # Создаем строку, которая будет показывать пользователю, что мы здесь вводим Имя
    # validators=[Required()] позволяет отслеживать, что написал пользователь
    # Базовые валидаторы
    # DataRequired() проверяет ввел ли пользователь какую-то ифнормацию в поле, является ли 
    # строка пустой
    # Email() проверяет является ли введенный email адрес действующим
    email = StringField("Почта", validators=[Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    # validators=[DataRequired()] указали, что это поле является обязательным
    # Галочка запомнить имя пароль
    remember_me = BooleanField('Запомнить')    
    #SubmitField позволяет отслеживать нажатие 
    submit = SubmitField('Войти')
    