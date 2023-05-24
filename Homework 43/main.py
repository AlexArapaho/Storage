from flask import Flask, render_template, url_for, session, redirect, request, g
import sqlite3
import os
from FDataBase import FDataBase

DATABASE = '/tmp/catalog.db'
DEBUG = True
SECRET_KEY = 'd5a781e8b1d7edd0c27ec4d9bc430fa556e40317'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'catalog.db')))
app.config['SECRET_KEY'] = 'd5a781e8b1d7edd0c27ec4d9bc430fa556e40317'

menu = [
    {'name': "Главная", 'url': 'index'},
    {'name': "Каталог", 'url': 'catalog'},
    {'name': 'Личный кабинет', 'url': 'account'},
    {'name': 'Обратная связь', 'url': 'contact'},
    ]

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html', title='Главная', menu=menu)

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db




@app.route('/catalog')
def catalog():
    db = get_db()
    dbase = FDataBase(db)
    x = dbase.get_items()
    return render_template('catalog.html', title='Каталог товаров', menu=menu, items=dbase.get_items())


@app.route("/item/<id_item>")
def show_item(id_item):
    db = get_db()
    dbase = FDataBase(db)
    item = dbase.get_item(id_item)
    return render_template('item.html', title='Карточка товара', item=item)


@app.route('/profile')
def profile():
    return render_template('profile.html', title='Личный кабинет', menu=menu)


@app.route('/account', methods=['POST', 'GET'])
def account():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['psw'] == '123321':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('account.html', title='Личный кабинет', menu=menu)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.route('/add_item', methods=["POST", "GET"])
def add_item():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        res = dbase.add_item(request.form.get('name'), request.form.get('description'), request.form.get('price'))
    return render_template('add_item.html', title="Добавление карточки товара", menu=menu)



@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()





if __name__ == '__main__':
    app.run(debug=True)