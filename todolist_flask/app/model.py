from . import db, login_manager
import datetime
from flask_login import UserMixin, AnonymousUserMixin
from markdown import markdown


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', backref='role')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guests', 'Administrators']))
        db.session.commit()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    role_id = db.Column(db.INTEGER, db.ForeignKey('roles.id')) #外键

    posts = db.relationship('Post', backref='author')
    comments = db.relationship('Comment', backref='author')


    @staticmethod
    def on_created(target, value, oldvalue, initiator):
        target.role = Role.query.filter_by(name='Guests').first()


class AnonymousUser(AnonymousUserMixin):
    @property
    def locale(self):
        return 'zh'
    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db.event.listen(User.name, 'set', User.on_created)



class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    body_html = db.Column(db.String)
    created = db.Column(db.DATETIME, index=True, default=datetime.datetime.now())

    comments = db.relationship('Comment', backref='post')
    author_id = db.Column(db.INTEGER, db.ForeignKey('users.id'))
    @staticmethod
    def on_body_change(target, value, oldvalue, initiator):
        if (value is None) or (value is ''):
            target.body_html = ''
        else:
            target.body_html = markdown(value)

db.event.listen(Post.body, 'set', Post.on_body_change)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.INTEGER, primary_key=True)
    body = db.Column(db.String)
    created = db.Column(db.DateTime, index=True, default=datetime.datetime.now())
    post_id = db.Column(db.INTEGER, db.ForeignKey('posts.id'))
    author_id = db.Column(db.INTEGER, db.ForeignKey('users.id'))


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.INTEGER, primary_key=True)
    content = db.Column(db.String)
    status = db.Column(db.String)
