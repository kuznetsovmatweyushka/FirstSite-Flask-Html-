from flask import Flask, render_template, redirect
from auth import LoginForm
from flask_login import login_user
from reg import RegisterForm
from data import db_session, users


app = Flask(__name__)
app.config['SECRET_KEY'] = 'world world world hello' # csrf-атаки


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    db_session.global_init('db/blogs.sqlite')
    form = LoginForm()
    if form.validate_on_submit():
        sessions = db_session.create_session()
        user = sessions.query(users.User).filter(users.User.email == form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember_me.data)
            return redirect('/bio', title = 'bio')
    return render_template('bio.html')


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    db_session.global_init('db/blogs.sqlite')
    form = RegisterForm()
    if form.validate_on_submit():
        sessions = db_session.create_session()
        try:
            user = users.User(
                name=form.name.data,
                email=form.email.data,
                telephone=form.telephone.data,
                password=form.password.data
            )
            user.set_password(form.password.data)
            sessions.add(user)
            sessions.commit()
        except:
            return render_template('reg.html', message='Такой пользователь есть!')
        return render_template('base.html', message='Вы авторизовались')
    return render_template('reg.html', form=form)

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
    db_session.global_init('db/blogs.sqlite')
    app.run()