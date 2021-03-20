from microblog.blog import blog
from flask import render_template
from microblog.blog.forms import PostForm

posts = [
    {
        "id": 1,
        "author": 'ak28',
        "date_posted": '27 Jun, 2012',
        "profile_pic": 'default.png',
        "body": 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem vitae deleniti voluptate veritatis aperiam ipsa cupiditate sed molestiae asperiores, molestias aspernatur pariatur maxime. Minima earum amet assumenda nisi similique esse.'
    },
    {
        "id": 12,
        "author": 'ak28',
        "date_posted": '27 Jun, 2012',
        "profile_pic": 'default.png',
        "body": 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem vitae deleniti voluptate veritatis aperiam ipsa cupiditate sed molestiae asperiores, molestias aspernatur pariatur maxime. Minima earum amet assumenda nisi similique esse.'
    },
    {
        "id": 1334,
        "author": 'ak28',
        "date_posted": '27 Jun, 2012',
        "profile_pic": 'default.png',
        "body": 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem vitae deleniti voluptate veritatis aperiam ipsa cupiditate sed molestiae asperiores, molestias aspernatur pariatur maxime. Minima earum amet assumenda nisi similique esse.'
    }
]

@blog.route('/')
def index():
    return render_template('blog/index.html', posts=posts)

@blog.route('/new')
def post():
    form = PostForm()
    return render_template('blog/create_post.html', form=form)