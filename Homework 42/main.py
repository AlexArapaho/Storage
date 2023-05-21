from flask import Flask, render_template, url_for, session, redirect, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'kanc7y3439kdkdru7t09ojd4ierng'

menu = [
    {'name': "Главная", 'url': 'index'},
    {'name': "Каталог", 'url': 'catalog'},
    {'name': 'Личный кабинет', 'url': 'account'},
    {'name': 'Обратная связь', 'url': 'contact'},
    ]

@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html', title='Главная', menu=menu)

@app.route('/catalog')
def catalog():
    return render_template('catalog.html', title='Каталог товаров', menu=menu)

@app.route('/profile')
def profile():
    return render_template('profile.html', title='Личный кабинет', menu=menu)

@app.route('/account', methods=['POST', 'GET'])
def account():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'buyer' and request.form['psw'] == '123321':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('account.html', title='Личный кабинет', menu=menu)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template('contact.html', title='Обратная связь', menu=menu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)




if __name__ == '__main__':
    app.run(debug=True)