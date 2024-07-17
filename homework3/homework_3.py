from flask import Flask, render_template, request, redirect, url_for
from homework3.homework_models import db, User
from homework3.homework_form import RegisterForm
import secrets
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
hex_key = secrets.token_hex(16)
print(hex_key)
app.config['SECRET_KEY'] = hex_key
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homework_users.sqlite3'
db.init_app(app)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/home/')
def home():
    return render_template('main.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        user = User(name, last_name, email, password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('register.html', form=form)


@app.route('/users/')
def users():
    users = User.query.all()
    context = {'users': users}
    return render_template('check_users.html', **context)

@app.route('/success/')
def success():
    return render_template('success.html')
@app.cli.command('db_init')
def db_init():
    with app.app_context():
        db.create_all()
        db.session.commit()
    print('DB INIT DONE')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
