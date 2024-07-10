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

if __name__ == '__main__':
    app.run(debug=True)