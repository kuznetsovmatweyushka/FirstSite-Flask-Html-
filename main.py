from flask import Flask, render_template

app = Flask(__name__)


# Создание главной страницы на сервере 
@app.route('/')
def main():
    return render_template('base.html', title='Mathew Bio')


@app.route('/bio')  # Создание первой страницы
def foto():
    return render_template('bio.html', title='My foto')

@app.route('/secondfoto')  # Создание второй страницы
def secondfoto():
    return render_template('secondfoto.html', title='My second foto')

app.run()
