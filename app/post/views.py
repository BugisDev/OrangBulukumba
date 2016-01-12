from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app.models.post import Post, Comment, Vote
from .forms import CommentForm
from app.core.db import db
from flask.ext.login import current_user, login_required

post_views = Blueprint('post', __name__, template_folder='../templates')

@post_views.route("/", methods=["GET", "POST"])
def home():
    posts = Post.query.all()
    vote = Vote
    comment = Comment
    if request.method == "POST" and request.form["vote"]:
        if not current_user.is_authenticated:
            flash("Please login to vote a post")
            return redirect(url_for('user.login'))
        voting = Vote(request.form["vote"], current_user.id)
        db.session.add(voting)
        db.session.commit()
    return render_template('index.html', **locals())

@post_views.route("/post/<slug>", methods=["GET", "POST"])
@login_required
def post(slug):
    post = Post.query.filter_by(slug=slug).first()
    vote = Vote#
    comments = Comment
    if not post:
        return abort(404)
    form = CommentForm()
    # Handle POST method for comment form
    if form.validate_on_submit():
        comments = Comment(post.id, current_user.id, form.desc.data)
        db.session.add(comments)
        db.session.commit()
    return render_template('post.html', **locals())

@post_views.route("/vote", methods=['GET', 'POST'])
def vote():
    post = Post.query.get(request.form['vote'])
    message = None
    if Vote.query.filter_by(id_user = current_user.id, id_post=post.id).first():
        message = "Kamu telah memberikan vote sebelumnya"
    else:
        vote = Vote( post.id, current_user.id)
        db.session.add(vote)
        db.session.commit()
        message = "Kamu telah memberikan vote"
    return redirect(url_for('.post', slug=post.slug, message=message))
