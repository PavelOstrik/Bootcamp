from flask import Flask, render_template
from auth import LoginForm

app = Flask(__name__)
# Позволяет предотвратить csrf-атаки, для этого мы задали секретный ключ
app.config['SECRET_KEY'] = 'world world world hello'
# manager = Manager(app) проверяет является ли пользователь зарегистрированным

# добавлением  methods=['GET', 'POST'] мы делаем отслеживание внутри сервера,
# чтобы мы поняли, что это непосредственно метод post
# GET отправляем пользователю какие то данные
# POST пользователь отправляет данные нам
@app.route('/', methods=['GET', 'POST'])
def main():
    form = LoginForm()    
    # Если нажата конпка submit
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        print(name, surname, email)
        return render_template('base.html', title='Главная страница',
                                message='Вы авторизовались!')
    return render_template('base.html', title='Главная страница', form=form)
                                          
                                      

if __name__ == '__main__':
    app.run()
