from flask import Flask, render_template, request, make_response

app = Flask(__name__)
@app.route('/')
def index():
    context = {
        'title': 'Home',
        'name': 'Nurzhan'
    }
    response = make_response(render_template('index.html',**context))
    response.headers['new_head'] = 'New-value'
    response.set_cookie('name', 'Nurzhan')
    return response
@app.route('/getcookie/')
def get_cookies():
    name = request.cookies.get('name')
    return f"Cookie: {name}"

if __name__ == '__main__':
    app.run(debug=True)