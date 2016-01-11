import datetime
from app.core.db import db
from flask.ext.bcrypt import generate_password_hash

class User_Type(db.Model):
    __tablename__ = 'user_type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.VARCHAR(10))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.VARCHAR(45))
    username = db.Column(db.VARCHAR(15), unique=True)
    password = db.Column(db.VARCHAR(128))
    email = db.Column(db.VARCHAR(30), unique=True)
    bio = db.Column(db.VARCHAR(20))
    picture = db.Column(db.VARCHAR(50))
    updatedtime = db.Column(db.DateTime)
    createdtime = db.Column(db.DateTime)
    deletedtime = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)
    last_login = db.Column(db.DateTime)
    id_type_user = db.Column(db.Integer, db.ForeignKey('user_type.id'))
    type_user = db.relationship('User_Type',
        backref=db.backref('user', lazy='dynamic'))

    def __init__(self, full_name, username, email, password):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        if self.id is None:
            self.createdtime = datetime.datetime.now()
            self.updatedtime = datetime.datetime.now()
            self.deleted = 0
            self.id_type_user = 5

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def is_anonymous(self):
        return False

    def __repr__(self):
        return "<Username: %s>"%self.username

class Social_Media(db.Model):
    __tablename__ = 'social_media'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(15))
    atr = db.Column(db.VARCHAR(2))
    createdtime = db.Column(db.DateTime)
    updatedtime = db.Column(db.DateTime)
    deletedtime = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)

class Social_Media_User(db.Model):
    __tablename__ = 'social_media_user'
    id = db.Column(db.Integer, primary_key=True)
    id_socmed = db.Column(db.Integer, db.ForeignKey('social_media.id'))
    social_media = db.relationship('Social_Media',
        backref=db.backref('socmed_user', lazy='dynamic'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
        backref=db.backref('socmed_user', lazy='dynamic'))
    value = db.Column(db.VARCHAR(45))
    createdtime = db.Column(db.DateTime)
    updatedtime = db.Column(db.DateTime)
    deletedtime = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)
