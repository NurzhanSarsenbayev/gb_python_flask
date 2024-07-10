from flask import Flask
from flask import render_template

app = Flask(__name__)

html = ("<h1>Hello my name is Nurzhan</h1>"
        "<p> This is my first Flask page<br>I'm still not sure how this works, but I'm trying my best!</p>")

@app.route('/')
@app.route('/<name>/')
def stranger(name='stanger'):
    return f'Hello {name.capitalize()}!'
    #return 42

@app.route('/Nurzhan/')
def nurzhan():
    return 'Hello Nurzhan!'

@app.route('/Anna/')
def anna():
    return 'Hello Anna!'

@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'File path for {file}'

@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Input number is {num}'

@app.route('/text/')
def text():
    return html

@app.route('/poems/')
def poems():
    poem = ['Вот не думал, не гадал.',
            "Программистом взял и стал.",
            "Хитрый знает он язык,",
            'Он к другому не привык.']
    txt = '<h1>A poem</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return txt

@app.route('/index/')
def html_index():
    context = {'name' : 'Nurzhan'}
    return render_template('index2.html', **context)

@app.route('/if/')
def show_if():
    context = {'title' : 'Ветвление',
               'user' : 'Nurzhan haxx0r',
               'number' : 1}
    return render_template('show_if.html', **context)

@app.route('/for/')
def show_for():
    context = {'title': 'Цикл',
               'poem': ['Вот не думал, не гадал.',
                       "Программистом взял и стал.",
                       "Хитрый знает он язык,",
                       'Он к другому не привык.']}
    # txt = '<h1>A poem</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return render_template('show_for.html', **context)

@app.route('/users/')
def users():
    _users = [{'name' : 'Nurzhan',
               'mail' : 'nurzhan@mail.com',
               'phone' : '87777777'},
              {'name': 'Nurzhan',
               'mail': 'nurzhan@mail.com',
               'phone': '87777777'},
              {'name': 'Nurzhan',
               'mail': 'nurzhan@mail.com',
               'phone': '87777777'}
              ]
    context = {'users' : _users,
               'title' : 'Точечная нотация'}

    return render_template('users.html', **context)
if __name__ == '__main__':
    app.run(debug=True)