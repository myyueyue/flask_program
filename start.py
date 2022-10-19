# 导入Flask
from flask import Flask,render_template

# 实例化Flask
app = Flask(__name__)

from student.views import user

# app给蓝图注册路由
app.register_blueprint(user)


# 自定义返回信息
@app.route('/')
def index():
    return render_template('head.html')


# 让Flask跑起来
app.run(debug=True)
