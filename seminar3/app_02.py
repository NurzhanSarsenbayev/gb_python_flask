from datetime import datetime
from flask import Flask, render_template
from seminar3.models_02 import db,Book,Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_list.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('base.html')


@app.cli.command('init_db')
def init_db():
    with app.app_context():
        db.create_all()
        print('Initialized the database.')
@app.cli.command('fill_db')
def fill_db():
    with app.app_context():
        author_1 = Author(name='John', last_name='Smith')
        author_2 = Author(name='Jane', last_name='Doe')
        db.session.add_all([author_1,author_2])
        db.session.commit()

        book_1 = Book(title= 'The First Book',  quantity= 3000, author_id = author_1.id)
        book_2 = Book(title= 'The Second Book',  quantity= 4000, author_id = author_2.id)
        book_3 = Book(title= 'The Third Book',  quantity= 1000, author_id = author_1.id)
        db.session.add_all([book_1,book_2,book_3])
        db.session.commit()

@app.route('/book_list/')
def book_list():
    books = Book.query.all()
    context = {'books' : books}
    return render_template('book_list.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
