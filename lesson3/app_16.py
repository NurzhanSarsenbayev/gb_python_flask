from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from form_3 import LoginForm

# import secrets

# print(secrets.token_hex())
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
