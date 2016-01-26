import datetime
from slugify import slugify
from app.core.db import db
from app.user.models import User
from unicodedata import normalize

class Post_type(db.Model):
    __tablename__ = 'post_type'
    id = db.Column(db.Integer, primary_key=True)
    post_type = db.Column(db.VARCHAR(10))
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
        backref=db.backref('Post_type', lazy='dynamic'))
    description = db.Column(db.VARCHAR(45))

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(50))
    slug = db.Column(db.VARCHAR(50))
    content = db.Column(db.VARCHAR(100))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
        backref=db.backref('Post', lazy='dynamic'))
    id_post_type = db.Column(db.Integer, db.ForeignKey('post_type.id'))
    post_type = db.relationship('Post_type',
        backref=db.backref('Post', lazy='dynamic'))
    createdtime = db.Column(db.DateTime)
    updatetime = db.Column(db.DateTime)
    deletedtime = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)

    def __init__(self, title, content, id_post_type, id_user):
        self.title = title
        self.content = content
        self.id_post_type = id_post_type
        self.id_user = id_user
        self.slug = slugify(unicode(self.title))
        self.createdtime = datetime.datetime.now()
        self.updatetime = datetime.datetime.now()
        self.deleted = 0

    def __repr__(self):
        return "<Post: %s>"%self.title

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    id_post = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post',
        backref=db.backref('Comment', lazy='dynamic'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
        backref=db.backref('Comment', lazy='dynamic'))
    desc = db.Column(db.VARCHAR(50))
    createdtime = db.Column(db.DateTime)
    updatetime = db.Column(db.DateTime)
    deletedtime = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)

    def __init__(self, id_post, id_user, desc):
        self.id_post = id_post
        self.id_user = id_user
        self.desc = desc
        self.createdtime = datetime.datetime.now()
        self.updatetime = datetime.datetime.now()
        self.deleted = 0

class Vote(db.Model):
    __tablename__ = 'vote'
    id = db.Column(db.Integer, primary_key=True)
    id_post = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post',
        backref=db.backref('Vote', lazy='dynamic'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
        backref=db.backref('Vote', lazy='dynamic'))
    createdtime = db.Column(db.DateTime)
    updatetime = db.Column(db.DateTime)
    deletedtime = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)

    def __init__(self, id_post, id_user):
        self.id_post = id_post
        self.id_user = id_user
        self.createdtime = datetime.datetime.now()
        self.updatetime = datetime.datetime.now()
        self.deleted = 0

    def __repr__(self):
        return "<Vote %s>"%self.post.title
