from flask import Flask, request,make_response,render_template,session,redirect,url_for
app = Flask(__name__)
app.secret_key = b"7a2fa7abbd58c5df6ac243404911b2a035d9f2aca123c7df8b56505e4095c201"

@app.route('/')
def index():
    if 'username' in session:
        return f"Hello {session['username']}"
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')

if __name__ == '__main__':
    app.run(debug=True)