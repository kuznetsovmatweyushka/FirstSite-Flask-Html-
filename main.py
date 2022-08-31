from flask import Flask, render_template
from auth import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'world world world hello'  # csrf - atacks


@app.route('/', methods=['GET', 'POST'])
def main():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        print(name, surname, email)
        return render_template('base.html', title='Главная страница',
                               message='Вы авторизовались!')
    return render_template('base.html', title='Главная страница',
                           form=form)

@app.route('/bio')  # Создание первой страницы
def foto():
    return render_template('bio.html', title='My foto')

@app.route('/secondfoto')  # Создание второй страницы
def secondFoto():
    return render_template('secondfoto.html', title='My second foto')

@app.route('/gitinstruction')  # Создание третьей страницы
def gitInstruction():
    return render_template('GitInstruction.md', title='My GitInstruction')

if __name__ == '__main__':
    app.run()
