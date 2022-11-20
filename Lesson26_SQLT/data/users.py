import datetime
import sqlalchemy
from sqlalchemy import orm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


# ORM модель позволяет обращаться к базе данных без SQL
# Создаем класс
class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    # Указываем имя таблицы
    __tablename__ = 'users'

    # Указываем какие есть столбцы
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    telephone = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    # Методы нашего класса, которые позволяют захешировать наш пароль
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    # Проверка пароля на правильность
    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
    
    # Метод, который будет возвращать нам данные
    def __repr__(self):
        return f'{self.id}, {self.name}, {self.telephone}, {self.email}'