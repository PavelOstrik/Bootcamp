from flask import Flask, render_template, redirect
from auth import LoginForm
from flask_login import LoginManager, login_user
from reg import RegisterForm
from data import db_session, users


app = Flask(__name__)
app.config['SECRET_KEY'] = 'world world world hello' # csrf-атаки


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('base.html')
# render_template('base.html') подключает шаблоны из соответствующей папки


@app.route('/login', methods=['GET', 'POST'])
def login():
    db_session.global_init('db/blogs.sqlite')
    form = LoginForm()
    if form.validate_on_submit():
        # Создаем сессию в базу данных
        sessions = db_session.create_session()
        # Берем нужные нам данные из таблицы и если они равны введенным то берем первое совпадение
        user = sessions.query(users.User).filter(users.User.email == form.email.data).first()
        # Проверяем введенный пароль
        if user and user.password == form.password.data:
            # Если все совпало, запоминаем нашего пользователя
            login_user(user, remember=form.remember_me.data)
            # Переадресовываем на определенный html файл, зная только путь к нему
            return redirect('/')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reg():
    db_session.global_init('db/blogs.sqlite')
    form = RegisterForm()
    if form.validate_on_submit():
        sessions = db_session.create_session()
        try:
            # Обращаемся к классу и перечисляем что мы будем запоминать в нашу базу данных
            user = users.User(
                name=form.name.data,
                email=form.email.data,
                telephone=form.telephone.data,
                password=form.password.data
            )
            user.set_password(form.password.data)
            # Запоминаем пользователя
            sessions.add(user)
            sessions.commit()
        except:
            return render_template('register.html', message='Такой пользователь есть!')
        return render_template('base.html', message='Вы авторизовались')
    return render_template('register.html', form=form) # form=form передаем эту форму в html


if __name__ == '__main__':
    # Подключаем нашу базу данных
    db_session.global_init('db/blogs.sqlite')
    app.run()