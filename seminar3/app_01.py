from flask import Flask, render_template, redirect, url_for
from seminar3.models_01 import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_list.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('main.html')


@app.cli.command('init_db')
def init_db():
    with app.app_context():
        db.create_all()
        print('Initialized the database.')


@app.cli.command('fill_table')
def create_tables():
    with app.app_context():
        faculty1 = Faculty(name='Computer Science')
        faculty2 = Faculty(name='Mathematics')
        faculty3 = Faculty(name='Physics')
        faculty4 = Faculty(name='Chemistry')
        db.session.add_all([faculty1, faculty2, faculty3, faculty4])
        db.session.commit()

        student1 = Student(name='John', last_name='Doe', age=20, gender='M',
                           faculty_id=faculty1.id)
        student2 = Student(name='Jane', last_name='Smith', age=22, gender='F',
                           faculty_id=faculty2.id)
        student3 = Student(name='Bob', last_name='Saget', age=22, gender='M',
                           faculty_id=faculty3.id)
        student4 = Student(name='Clarissa', last_name='Rowan', age=22, gender='F',
                           faculty_id=faculty4.id)
        student5 = Student(name='Alex', last_name='Hirsch', age=22, gender='M',
                           faculty_id=faculty1.id)
        db.session.add_all([student1, student2, student3, student4, student5])
        db.session.commit()
    print('Initialized the database.')


@app.route('/student_list/')
def student_list():
    students = Student.query.all()
    context = {'students': students}
    return render_template('student_list.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
#