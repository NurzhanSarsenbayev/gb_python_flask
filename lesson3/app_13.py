from datetime import timedelta, datetime

from flask import Flask, render_template, jsonify
from lesson3.models_05 import db, User,Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/mydatabase.db'

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/')
def data():
    return f'Your data!'

@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)

@app.route('/users/<int:username>/')
def user_by_username(username):
    users = User.query.filter_by(username=username).all()
    context = {'users': users}
    return render_template('users.html',**context)

@app.route('/posts/author/<int:user_id>/')
def user_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content, 'created at': post.created_at} for post in posts]
        )
    else:
        return jsonify({'error': 'No posts found.'}),404
@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content, 'created at': post.created_at} for post in posts]
        )
    else:
        return jsonify({'error': 'No posts found.'}),404

if __name__ == '__main__':
    app.run(debug=True)