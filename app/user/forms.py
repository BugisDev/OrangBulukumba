from flask_wtf import Form
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, TextAreaField, SelectField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .models import User
from app.post.models import Post_type
from flask.ext.bcrypt import check_password_hash

class LoginForm(Form):
    username = StringField('Username', validators=[validators.Required('Username tidak boleh kosong')])
    password = PasswordField('Password', validators=[validators.Required('Username tidak boleh kosong')])

    #Add a validation when Logged In
    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user is None or not user:
            self.username.errors.append('Unknown username')
            return False
        if not check_password_hash(user.password, self.password.data):
            self.password.errors.append('Invalid password')
            return False
        self.user = user
        return True

class RegisterForm(Form):
    full_name = StringField('Full Name', validators=[validators.Required('Nama tidak boleh kosong')])
    username = StringField('Username', validators=[validators.Required('Username tidak boleh kosong')])
    email = StringField('Email', validators=[validators.Required('Email tidak boleh kosong')])
    password = PasswordField('Password', validators=[validators.Required('Password Tidak boleh kosong'),
                                                     validators.EqualTo('confirm', message='Password harus sama')])
    confirm = PasswordField('Ulangi Password')

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        if User.query.filter_by(username=self.username.data).first():
            self.username.errors.append("Username Telah digunakan")
            return False

        if User.query.filter_by(email=self.email.data).first():
            self.email.errors.append("Email yang anda masukkan telah terdaftar")
            return False
        return True

class CreatePost(Form):
    title = StringField('title', validators=[validators.Required('Judul tidak boleh kosong')])
    content = TextAreaField('Content', validators=[validators.Required('Konten tidak boleh kosong'),
                                                   validators.Length(max=100, message="Konten maksimal 100 karakter")])
    post_type = SelectField('Type', coerce=int)


class ProfileForm(Form):
    picture = FileField('Foto', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    full_name = StringField('Full Name', validators=[validators.Required('Nama tidak boleh kosong')])
    username = StringField('Username', validators=[validators.Required('Username tidak boleh kosong')])
    email = StringField('Email', validators=[validators.Required('Email tidak boleh kosong')])
    bio = TextAreaField('Bio')
