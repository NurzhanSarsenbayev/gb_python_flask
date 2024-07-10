from pathlib import Path, PurePath

from flask import Flask, render_template, url_for, request, abort, redirect, flash,make_response
from markupsafe import escape
from werkzeug.utils import secure_filename

# import secrets
#
# secrets.token_hex()

app = Flask(__name__)
app.secret_key = b"7a2fa7abbd58c5df6ac243404911b2a035d9f2aca123c7df8b56505e4095c201"


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/<path:file>/')
# def get_file(file):
#     print(file)
#     # return f"Path to your file is {file}!"
#     return f'Path to your file is {escape(file)}!'


@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}!<br>'
    text += f"Функция {url_for('test_url', num = 42) = }<br>"
    text += f"Функция {url_for('test_url', num = 42, data = 'new_data') = }<br>"
    text += f"Функция {url_for('test_url', num= 42, data = 'new_data', pi = 3.14515) = }<br>"
    return text


@app.route('/about/')
def about():
    context = {
        'title': 'About',
        'name': 'Nurzhan'
    }
    return render_template('about.html', **context)


@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок!<br>'
    return f'{text} {request.args}'


# @app.route('/submit', methods = ['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         return f'Hello, {name}'
#     return render_template('form.html')

@app.get('/submit')
def submit_get():
    return render_template('form.html')


@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello, {name}!'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


def get_blog(id=None):
    return None


@app.route('/blog/<int:id>/')
def get_blog_by_id(id):
    result = get_blog(id)
    if result is None:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Page not found',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


@app.errorhandler(500)
def server_error(e):
    app.logger.warning(e)
    context = {
        'title': 'Server Error',
        'url': request.base_url,
    }
    return render_template('500.html', **context), 500


@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route('/external/')
def external_redirect():
    return redirect('https://www.python.org/')


@app.route('/hello/<name>/')
def hello(name):
    return f'Hello, {name}'


@app.route('/redirect/<name>/')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Enter your name!','danger')
            return redirect(url_for('form'))
        flash("Form sent successfully", 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
