import sqlalchemy
import databases

DATABASE_URL = "sqlite:///homework_6.db"
metadata = sqlalchemy.MetaData()

items = sqlalchemy.Table(
    'items',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('description', sqlalchemy.String),
    sqlalchemy.Column('price', sqlalchemy.Integer),
)
users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('last_name', sqlalchemy.String),
    sqlalchemy.Column('email', sqlalchemy.String),
    sqlalchemy.Column('password', sqlalchemy.String),
)
orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('item_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('items.id')),
    sqlalchemy.Column('date', sqlalchemy.DateTime),
    sqlalchemy.Column('status', sqlalchemy.BOOLEAN)
)