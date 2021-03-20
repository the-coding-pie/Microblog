from microblog.auth import auth
from flask import render_template, flash, redirect, abort, url_for, request
from microblog.auth.forms import LoginForm, RegistrationForm
from microblog.auth.models import User
from microblog import db, bcrypt
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("You account has been created!", category="success")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not bcrypt.check_password_hash(user.password_hash, form.password.data):
            flash('Invalid username or password', category="danger")
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        flash("You are now logged in!", category="success")
        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('blog.index')
        
        return redirect(next_page)
    return render_template('auth/login.html', title='Login', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))