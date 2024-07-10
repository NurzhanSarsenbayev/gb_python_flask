from urllib import request

from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
import secrets

print(secrets.token_hex())
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
csrf = CSRFProtect(app)
@app.route('/')
def index():
    return 'Hello World!'

@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def form():
    return 'No CRRF Protection!'
if __name__ == '__main__':
    app.run(debug=True)
