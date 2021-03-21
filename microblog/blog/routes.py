from microblog.blog import blog
from flask import render_template, flash, redirect, url_for, abort, request
from microblog.blog.forms import PostForm
from flask_login import login_required
from microblog.blog.models import Post
from flask_login import current_user
from microblog import db

@blog.route('/')
@login_required
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('blog/index.html', posts=posts, title='Home')

@blog.route('/post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, author_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('New Post Added!', category="success")
        return redirect(url_for('blog.index'))
    return render_template('blog/create_post.html', form=form, title='Create Post')

@blog.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/post_detail.html', title='Post Detail', post=post)

@blog.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
def post_update(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.body = form.body.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('blog.index'))
    elif request.method == 'GET':
        form.body.data = post.body

    return render_template('blog/create_post.html', title='Post Update', form=form)

@blog.route('/post/<int:post_id>/delete', methods=['POST'])
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('blog.index'))