from flask import Blueprint, session, redirect, url_for
from flask import render_template, request

from .model import database_session, User

# 注册蓝图
user = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')


@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username, password]):
            msg = '请填写完整信息'
            return render_template('login.html', msg=msg)
        user = database_session.query(User).filter_by(username=username, password=password).first()
        database_session.close()
        if user:
            return render_template('login.html')
        else:
            msg = '账号或者密码错误'
            return render_template('login.html', msg=msg)


@user.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == "POST":
        username = request.form.get('username')
        pwd1 = request.form.get('pwd1')
        pwd2 = request.form.get('pwd2')
        flag = True
        if not all([username, pwd1, pwd2]):
            msg, flag = '请填写完整信息', False
        if len(username) > 50:
            msg, flag = '用户名太长', False
        if pwd1 != pwd2:
            msg, flag = '两次密码不一致', False
        if not flag:
            return render_template('register.html', msg=msg)
        users = database_session.query(User).filter_by(username=username, password=pwd1).first()
        if users:
            msg = '用户已存在'
            return render_template('register.html', msg=msg)
        Person = User(username=username, password=pwd1)
        database_session.add(Person)
        database_session.commit()
        database_session.close()
        return render_template('login.html')


from utils.is_login import is_login


@user.route('/logout/', methods=['GET'])
@is_login
def logout():
    if request.method == 'GET':
        session.clear()
        return redirect(url_for('user.login'))
