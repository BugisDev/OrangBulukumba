from flask_wtf import Form
from wtforms import TextAreaField, validators

class CommentForm(Form):
    desc = TextAreaField('Komentar', validators=[validators.Required('Komentar tidak boleh kosong')])
