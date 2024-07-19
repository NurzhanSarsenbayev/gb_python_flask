from flask import Flask, render_template,request,redirect,url_for
from seminar3.models_04 import db,User
from seminar3.form_04 import RegistrationForm
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SECRET_KEY'] = 'secret'
db.init_app(app)
csrf = CSRFProtect(app)

@app.cli.command('db_init')
def db_init():
    db.create_all()
    print('db init done')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username =form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print(username, email, password)
    return render_template('register.html', form=form)
@app.route('/users/')
def users():
    users = User.query.all()
    context = {'users':users}
    return render_template('users.html', **context)

if __name__ == '__main__':
    app.run(debug=True)