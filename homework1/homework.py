from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/coats/')
def coats():
    _coats = [{'color':['black coat' , 'white coat', 'plaid coat']}]
    context = {'title': 'Coats',
               'coats': _coats}
    return render_template('coats.html',**context)


@app.route("/shirts/")
def shirts():
    context = {'title': 'Shirts',
               'shirts' : ['black shirt', 'white shirt', 'plaid shirt']}
    return render_template('shirts.html',**context)


@app.route('/pants/')
def pants():
    _pants = ['black pants', 'white pants', 'plaid pants']
    context = {'title': 'Pants',
               'pants': _pants}
    return render_template('pants.html',**context)


if __name__ == '__main__':
    app.run(debug=True)
