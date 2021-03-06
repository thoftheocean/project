#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
import config
from flask_bootstrap import Bootstrap
from flask_nav import *
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babel import gettext as _,Babel


#获取当前文件的决定路径
from os import path
basedir = path.abspath(path.dirname(__file__))

#模板
bootstrap = Bootstrap()
#数据库
db = SQLAlchemy()
#导航栏
nav = Nav()
#全球化
babel = Babel()

#登录
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



def create_app(config_name='default'):
    app = Flask(__name__)
    # 读取外部的配置文件
    app.config.from_pyfile('config')
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    #babel配置文件
    # app.config.from_object(config[config_name])

    nav.register_element('top', Navbar(
                        View(u'主页', 'main.home'),
                        View(u'关于', 'main.about'),
                        View(u'服务', 'main.service'),
                        View(u'登录', 'auth.login'),
                        View(u'注册', 'auth.register'),
                        View(u'todolist', 'main.todolist')
    ))

    db.init_app(app)
    bootstrap.init_app(app)
    nav.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app)

    from app.auth import auth as auth_blueprint
    from app.main import main as main_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth', static_folder='static')
    app.register_blueprint(auth_blueprint, static_folder='static')
    app.register_blueprint(main_blueprint)
    return app


