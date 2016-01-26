from flask_wtf import Form
from wtforms import TextAreaField, validators, SubmitField
from flask.ext.login import current_user
from .models import Post, Comment, Vote

class CommentForm(Form):
    desc = TextAreaField('Komentar', validators=[validators.Required('Komentar tidak boleh kosong')])
