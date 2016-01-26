import datetime
import config
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.ext.uploads import UploadSet, IMAGES
from werkzeug import secure_filename
from app.core.db import db
from .models import User
from app.post.models import Post, Post_type, Vote, Comment
from .forms import RegisterForm, LoginForm, CreatePost, ProfileForm
from flask.ext.login import login_user, logout_user, login_required, current_user

user_views = Blueprint('user', __name__, template_folder='../templates/user', static_folder='../static')

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
    #check session
    if current_user.is_authenticated:
        return redirect(url_for('.my_profile'))
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
@login_required
def create_post():
    form = CreatePost()
    #set dynamic for post type choices
    form.post_type.choices = [(a.id, a.post_type) for a in Post_type.query.all()]
    #Handle Post method
    if form.validate_on_submit():
        post = Post(form.title.data, form.content.data, form.post_type.data, current_user.id)
        db.session.add(post)
        db.session.commit()
        flash("Postingan anda telah tersimpan")
        return redirect(url_for('.create_post'))
    return render_template('create_post.html', form=form)

@user_views.route('/user/<username>', methods=['GET', 'POST'])
def profile(username):
    user = User.query.filter_by(username = username).first_or_404()
    picture = user.picture if user.picture else 'default.png'
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
    return render_template('profile.html', **locals())

@user_views.route('/profile')
@login_required
def my_profile():
    user = User.query.get(current_user.id)
    picture = user.picture if user.picture else 'default.png'
    return render_template('my_profile.html', **locals())

@user_views.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    form = ProfileForm()
    user = User.query.get(current_user.id)
    picture = user.picture if user.picture else 'default.png'
    if form.validate_on_submit():
        if form.picture.data:
            filename = secure_filename(form.picture.data.filename)
            form.picture.data.save(config.base.IMG_USER + filename)
            user.picture = filename
        user.full_name = form.full_name.data
        user.username = form.username.data
        user.email = form.email.data
        user.bio = form.bio.data
        db.session.commit()
    return render_template("edit_profile.html", **locals())

@user_views.route('/logout/')
@login_required
def logout():
    flash('logout sukses')
    logout_user()
    return redirect(url_for('user.login'))
