from flask import Flask
from login_demo import login    # 从分路由倒入路由函数
from register_demo import register
from admin import admin
from user import user
app = Flask(__name__)


# 注册蓝图 第一个参数 是蓝图对象
app.register_blueprint(login,url_prefix='/login')
app.register_blueprint(register, url_prefix='/register')
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')
@app.route('/')
def hello_world():
    return 'Hellorld!'


if __name__ == '__main__':

    app.run()