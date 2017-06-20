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
    query = Post.query.order_by(Post.created.desc())
    pagination = query.paginate(page_home, per_page=20, error_out=False)
    posts = pagination.items
    return render_template('index.html',
                           title=u"欢迎来到H的博客",
                           post=posts,
                           pagination=pagination)

@main.route('/service/')
def service():
    return 'service'

@main.route('/about/')
def about():
    return 'about'

@main.route('/product/')
def product():
    return 'product'


@main.route('/post/<int:id>', methods=['Get', 'Post'])
def post(id):
    #Detail 详细页
    post = Post.query.get_or_404(id)
    #评论窗口
    form = CommentForm()
    #保存评论
    if form.validate_on_submit():
        comment = Comment(body=form.body.data, post=post)
        db.session.add(comment)
        db.session.commit()
    #评论列表
    return render_template('posts/detail.html',
                            title=post.title,
                            form=form,
                            post=post)

@main.route('/edit', methods=['GET', 'POST'])
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
# @login_required
def edit(id=0):
    form = PostForm()

    # if id == 0:
    #     post = Post(author=current_user)
    #
    # else:
    #     post = Post.query.get_or_404(id)

    post = Post()

    if form.validate_on_submit():
        post.body = form.body.data
        post.title = form.title.data

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('.post', id=post.id))

    form.title.data = post.title
    form.body.data = post.body

    title = _(u'添加新文章')
    if id > 0:
        title = _(u'编辑 - %(title)', title=post.title)

    return render_template('posts/edit.html',
                           title=title,
                           form=form,
                           post=post)


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


@main.route('/todolist/', methods=['GET', 'POST'] )
def todolist():
    add_form = AddEventForm()
    events = db.session.query(Event.content).all()
    # events  = Event.query.get(1).content


    if add_form.validate_on_submit():
        event = Event(content=add_form.content.data)
        db.session.add(event)
        db.session.commit()
        flash('添加事件成功')
        return redirect(url_for('main.todolist'))



    return render_template('todolist.html',
                           title='todolist页面',
                           add_form=add_form,
                           events=events)
@main.route('/')
def show():
    events=Event.query.filter_by(id=current_user.id).all()
    if events is None:
        flash('你还未添加任何事项')
    return render_template('todolist.html', events=events)
@main.route('/edit_event')
def edit_event(id):
    event = Event.query.get_or_404(id)
    edit_form = EditEventForm()
    if edit_form.validate_on_submit():
        event.content=edit_form.content.data
        db.session.add(event)
        flash('事件更新')
    edit_form.content.data=event.content
    return render_template('todolist2.html', title='todolist页面')

@main.route('/edit_event')
def delet_event(id):
    event = Event.query.get_or_404(id)
    if event:
        event.completion = True
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('main.todolist'))