from flask import Flask, render_template, request, redirect, url_for, make_response, session

app = Flask(__name__)

@app.route('/')
def home():
    context = {
        'title': 'Home',
    }
    return render_template('index.html',**context)
@app.route('/cookie_page/', methods=['GET','POST'])
def cookie_page():
    context = {
        'title': 'Cookie page',
    }
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['mail']
        response = make_response(redirect(url_for('greetings')))
        response.headers['new_head'] = 'New-value'
        response.set_cookie('name', name)
        response.set_cookie('mail', mail)
        return response
    return render_template('cookie_page.html', **context)

@app.route('/greetings/', methods=['GET','POST'])
def greetings():
    context = {
        'title': 'Greetings',
        'name' : request.cookies.get('name'),
        'mail' : request.cookies.get('mail'),
    }
    if request.method == 'POST':
        resp = make_response(redirect(url_for('home')))
        resp.set_cookie('name', '', expires=0)
        resp.set_cookie('mail', '', expires=0)
        return resp
    return render_template('greetings.html', **context)

if __name__ == '__main__':
    app.run(debug=True)

