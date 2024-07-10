from datetime import datetime

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/about/")
def about():
    return 'about'


@app.route("/contact/")
def contact():
    return 'contact'


@app.route("/<int:num1>/<int:num2>")
def sum(num1: int,num2: int):
    return str(num1 + num2)

# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.
@app.route("/string/<string:word>")
def length_of_word(word: str):
    return str(len(word))

@app.route("/index/")
def html():
    return render_template('index_seminar.html')

@app.route("/students/")
def students():
    _students = [{"name" : 'Nurzhan',
                 'surname' : 'Sarsenbayev',
                 'age' : '33',
                 'gpa' : "3.4"},
                {"name": 'Nurzhan2',
                 'surname': 'Sarsenbayev2',
                 'age': '33',
                 'gpa': "3.4"},
                {"name": 'Nurzhan3',
                 'surname': 'Sarsenbayev3',
                 'age': '33',
                 'gpa': "3.4"}
                ]
    context = {'students' : _students,
               'title' : 'Students table'}
    return render_template('students_seminar.html',**context)

@app.route('/news/')
def news():
    news_block = [
        {
            'title' : 'News 1',
            'description' : 'Description 1',
            'date' : datetime.now().strftime('%H:%M - %d.%m.%Y')

        },
        {
            'title': 'News 2',
            'description': 'Description 2',
            'date': datetime.now().strftime('%H:%M - %d.%m.%Y')

        },
        {
            'title': 'News 3',
            'description': 'Description 3',
            'date': datetime.now().strftime('%H:%M - %d.%m.%Y')

        }
    ]
    return render_template('news_seminar.html', news_block = news_block)


if __name__ == "__main__":
    app.run()