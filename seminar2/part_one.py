from pathlib import PurePath, Path
from venv import logger

from markupsafe import escape
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html', title="Main Page")


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return redirect(url_for('greeting', name=name))


@app.route('/greeting')
def greeting():
    name = request.args.get('name')
    return render_template('greeting.html', name=name, title="Greeting")


@app.route('/img_page/')
def img_page():
    return render_template('img_page.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"File {escape(file_name)} uploaded to server"
    return render_template('upload.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    context = {
        'title' : 'Login Page',
    }
    user = {
        'login' : 'a',
        'password' : '123'
    }
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == user['login'] and password == user['password']:
            return f"Login Successful"
        else:
            return f"Login Failed"
    return render_template('login.html', **context)

@app.route('/word_count', methods=['GET', 'POST'])
def word_count():
    if request.method == 'POST':
        text = request.form.get('text')
        word_count = len(text.split()) if text else 0
        return f"Word Count: {word_count}"
    context = {
        'title': 'Word Count',
    }
    return render_template('word_count.html', **context)

@app.route('/basic_math', methods=['GET', 'POST'])
def basic_math():
    math = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        'add': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
        'mul': lambda x, y: x * y,
        'div': lambda x, y: x / y,
    }
    context = {
        'title': 'Basic Math',
    }
    if request.method == 'POST':
        number_a = request.form.get('number_a')
        number_b = request.form.get('number_b')
        math_op = request.form.get('math_operation')

        try:
            number_a = int(number_a)
            number_b = int(number_b)
        except ValueError:
            return "Inputs must be integers"

        if math_op in math:
            math_operation = math[math_op]
            if (math_op == '/' or math_op == 'div') and number_b == 0:
                return f"Division by zero"
            result = math_operation(number_a, number_b)
            return f'{number_a} {math_op} {number_b} = {result}'
        else:
            return "Invalid operation"
    return render_template('basic_math.html', **context)
@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    _AGE = 18
    context = {
        'title': 'Check Age',
    }
    if request.method == 'POST':
        age = request.form.get('age')
        if int(age) < _AGE:

            abort(403)
        else:
            return f'Age is {age}. You may procced'
    return render_template('check_age.html', **context)

@app.errorhandler(403)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': '404 Page',
        'url' : request.url,
    }
    return render_template('403.html',**context), 403
if __name__ == '__main__':
    app.run(debug=True)
