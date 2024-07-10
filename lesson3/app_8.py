from flask import Flask
from lesson3.models_05 import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    return 'Hello World!'


@app.cli.command('init-db')
def init_db():
    with app.app_context():
        db.create_all()
        print('Initialized the database.')


@app.cli.command('add-john')
def add_john():
    user = User(username="john", email="john@example.com")
    db.session.add(user)
    db.session.commit()
    print('Added john.')


@app.cli.command('edit-john')
def edit_john():
    user = User.query.filter_by(username="john").first()
    user.email = 'new_email@example.com'
    db.session.commit()
    print('Edited john.')


@app.cli.command('delete-john')
def delete_john():
    user = User.query.filter_by(username="john").first()
    db.session.delete(user)
    db.session.commit()
    print('Deleted john.')


if __name__ == '__main__':
    app.run(debug=True)
