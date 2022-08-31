from flask import Flask, render_template
from auth import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'world world world hello'  # csrf - atacks


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('base.html', title='Главная страница')


@app.route('/login', methods=['GET', 'POST'])  # Создание первой страницы
def login():
    return render_template('login.html', title='Мой профиль')


@app.route('/reg', methods=['GET', 'POST'])  # Создание второй страницы
def registration():
    return render_template('reg.html', title='Регистрация')


@app.route('/gitinstruction')  # Создание третьей страницы
def gitInstruction():
    return render_template('GitInstruction.md', title='My GitInstruction')


if __name__ == '__main__':
    app.run()
