import datetime
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.core.db import db
from app.models.user import User
from app.models.post import Post, Post_type, Vote, Comment
from .forms import RegisterForm, LoginForm, CreatePost
from flask.ext.login import login_user, logout_user, login_required, current_user

user_views = Blueprint('user', __name__, template_folder='../../templates')

@user_views.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('post.home'))
    form = RegisterForm()
    # handling POST method
    if form.validate_on_submit():
        user = User(form.full_name.data, form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Aku anda sudah terdaftar, silahkan login")
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)

@user_views.route("/login/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('post.home'))
    form = LoginForm()
    # handling post method
    if form.validate_on_submit():
        user = form.user
        user.last_login = datetime.datetime.now()
        db.session.commit()
        login_user(user)
        return redirect(url_for('post.home'))
    # handle get method
    return render_template('login.html', form=form)


@user_views.route('/create_post/', methods=['GET', 'POST'])
def create_post():
    #check session
    if not current_user.is_authenticated:
        flash('Kamu harus login untuk membuat postingan')
        return redirect(url_for('.login'))
    form = CreatePost()
    form.post_type.choices = [(a.id, a.post_type) for a in Post_type.query.all()]
    #Handle Post method
    if form.validate_on_submit():
        post = Post(form.title.data, form.content.data, form.post_type.data, current_user.id)
        db.session.add(post)
        db.session.commit()
        flash("Postingan anda telah tersimpan")
        return redirect(url_for('.create_post'))
    return render_template('create_post.html', form=form)

@user_views.route('/<username>', methods=['GET', 'POST'])
def profile(username):
    if not current_user.is_authenticated:
        flash('Kamu harus login untuk melihat halaman ini')
        return redirect(url_for('.login'))
    user = User.query.filter_by(username = username).first_or_404()
    posts = Post.query.filter_by(id_user=user.id).all()
    vote = Vote
    comment = Comment
    if request.method == "POST" and request.form["vote"]:
        if not current_user.is_authenticated:
            flash("Please login to vote a post")
            return redirect(url_for('user.login'))
        voting = Vote(request.form["vote"], current_user.id)
        db.session.add(voting)
        db.session.commit()
    return render_template('my_profile.html', **locals())

@user_views.route('/profile')
def my_profile():
    if not current_user.is_authenticated:
        flash('Kamu harus login untuk melihat halaman ini')
        return redirect(url_for('.login'))
    return render_template('profile.html')


@user_views.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('post.home'))
