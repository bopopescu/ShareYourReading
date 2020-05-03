# encoding: utf-8

from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.Integer, nullable=False)


class Book(db.Model):
    __tablename__ = 'book'
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(200), nullable=False)


class Post(db.Model):
    __tablename__ = 'post'
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_title = db.Column(db.String(200), nullable=False)
    post_content = db.Column(db.Text, nullable=False)
    # now() is work to get the first time that the server run
    # now is to get current time when create a new model
    post_time = db.Column(db.DateTime, default=datetime.now)
    comment_num = db.Column(db.Integer, nullable=False)

    author = db.relationship('User', backref=db.backref('posts'))
    book = db.relationship('Book', backref=db.backref('posts'))


class Comment(db.Model):
    __tablename__ = 'comment'
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_content = db.Column(db.String(2000), nullable=False)

    post = db.relationship('Post', backref=db.backref('comments'))
    author = db.relationship('User', backref=db.backref('comments'))

# Harry Potter and the Order of the Phoenix (Harry Potter, #5) 2
# Word Power Made Easy 827597
