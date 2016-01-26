from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from .models import Post, Comment, Vote
from .forms import CommentForm
from app.core.db import db
from flask.ext.login import current_user, login_required

post_views = Blueprint('post', __name__, template_folder='../templates')

@post_views.route("/", methods=["GET", "POST"])
def home():
    posts = Post.query.all()
    return render_template('home.html', **locals())

@post_views.route("/post/<slug>", methods=["GET","POST"])
def post(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    form = CommentForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("Please login to give some comment")
            return redirect(url_for('user.login'))
        comments = Comment(post.id, current_user.id, form.desc.data)
        db.session.add(comments)
        db.session.commit()
        comment_msg = "Komentar berhasil dikirim"
        return redirect(url_for('.post', slug=post.slug))
    return render_template('post.html', **locals())

@post_views.route("/post/vote", methods=["POST"])
@login_required
def vote():
    post = Post.query.get(request.form["vote"])
    if not post:
        return abort(404)
    if Vote.query.filter_by(id_post=post.id, id_user=current_user.id).first():
        flash("Kamu hanya bisa melakukan vote satu kali")
    else:
        db.session.add(Vote(post.id, current_user.id))
        db.session.commit()
        flash("Vote sukses")
    return redirect(url_for('.post', slug=post.slug))
