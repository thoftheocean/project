#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import render_template, request, flash, redirect, url_for,current_app,abort
from . import main
from .. import db
from ..model import Post, Comment, Event
from flask_login import login_required, current_user
from app.auth.forms import CommentForm, PostForm, AddEventForm, EditEventForm
from flask_babel import gettext as _

@main.route("/")
def home():
    page_home = request.args.get('page', 1, type=int)
    query = Post.query.order_by(Post.created.asc())
    pagination = query.paginate(page_home, per_page=20, error_out=False)
    posts = pagination.items

    # posts = db.session.query(Post.id, Post.title, Post.body_html).all()

    return render_template('home.html',
                           title=u"欢迎来到H博客",
                           posts=posts,
                           pagination=pagination)


@main.route("/user",  methods=['POST', 'GET'])
def userpage():

    try:
        posts = Post.query.filter(Post.author_id == current_user.id).all()
        return render_template('userpage.html', posts=posts)
    except AttributeError:
        return redirect(url_for('auth.login'))



@main.route('/post/<int:id>', methods=['Get', 'Post'])
def post(id):
    #Detail 详细页
    post = Post.query.get_or_404(id)
    #评论窗口
    form = CommentForm()
    #保存评论
    try:
        if form.validate_on_submit():
            comment = Comment(body=form.body.data, post=post, author=current_user)
            db.session.add(comment)
            db.session.commit()
    except AttributeError:
        return redirect(url_for('auth.login'))

    #评论列表
    return render_template('posts/detail.html',
                            title=post.title,
                            form=form,
                            post=post)


@main.route('/edit', methods=['GET', 'POST'])
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit():
    form = PostForm()
    if form.validate_on_submit():
        print('hello')
        post=Post(title=form.title.data, body=form.body.data, author=current_user)
        print(post)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.post', id=post.id))
    posts = db.session.query(Post.id, Post.title, Post.body).all()

    return render_template('posts/edit.html',
                           form=form,
                           post=posts)



# @main.route('/edit', methods=['GET', 'POST'])
# @main.route('/edit/<int:id>', methods=['GET', 'POST'])
# def edit(id=0):
#     form = PostForm()
#     if form.validate_on_submit():
#         print('hello')
#         post=Post(title=form.title.data, body=form.body.data)
#         print(post)
#         db.session.add(post)
#         db.session.commit()
#
#         return redirect(url_for('.post', id=post.id))
#     title = u'编辑'
#     posts = db.session.query(Post.id, Post.title, Post.body).all()
#
#     return render_template('posts/edit.html',
#                            title=title,
#                            form=form,
#                            post=posts)




# @main.route('/shoutdown')
# def shutdown():
#     if not current_app.testing:
#         abort(404)
#
#     shoutdown = request.environ.get('werkzeug.server.shutdown')
#     if not shoutdown:
#         abort(500)
#
#     shoutdown()
#     return u'正在关闭服务端进程...'



@main.route('/todolist/', methods=['GET', 'POST'])
def todolist():
    add_form = AddEventForm()
    events = db.session.query(Event.id, Event.content, Event.status).all()

    if add_form.validate_on_submit():
        #添加
        event = Event(content=add_form.content.data, status='未完成')
        db.session.add(event)
        db.session.commit()
        flash('添加事件成功')
        return redirect(url_for('main.todolist'))

    if request.args.get('operate') == "delete":
        # 删除
        delete_id = request.args.get('id')
        delete_event = Event.query.filter(Event.id == delete_id).first()
        if delete_event != None:
            db.session.delete(delete_event)
            db.session.commit()
        return redirect(url_for('main.todolist'))

    if request.args.get('operate') == "save":
        # 保存编辑
        event = Event.query.filter(Event.id == request.args.get('id')).first()
        event.content = request.args.get('value')
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('main.todolist'))
        #保存状态
    if request.args.get('status'):
        event = Event.query.filter(Event.id == request.args.get('id')).first()
        event.status = request.args.get('status')
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('main.todolist'))

    return render_template('todolist.html',
                            title='todolist页面',
                            add_form=add_form,
                            events=events,
                            )

