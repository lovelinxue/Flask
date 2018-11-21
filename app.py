from flask import Flask, redirect, url_for, abort
from flask import request
from flask import make_response # 读取cookie使用
from werkzeug.routing import BaseConverter
from flask import render_template
from os import path # 文件存储使用
from werkzeug.utils import secure_filename


# 正则表达式相关类
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app = Flask(__name__)

# 加载一下正则表达
app.url_map.converters['regex'] = RegexConverter


@app.route('/')
def hello_world():
    print(url_for('article', id=123))
    response = make_response(render_template('form.html'))
    response.set_cookie('username', '')
    return response


@app.route('/JD/', methods=['GET', 'POST'])
def JDAction():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('signin_from'), code=301)
    else:
        return name


@app.route('/article/<id>/')
def article(id):
    return '%s article detail' % id


@app.route('/index/<userName>')
def index(userName=None):
    user = {'name': userName}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='title', user=user, posts=posts)


@app.route('/signin', methods=['GET'])
def signin_from():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '123123':
        return render_template('signin-ok.html', username=username, password=password)
    return render_template('form.html', message='用户名或者密码输入错误', username=username)


@app.route('/project/', methods=["GET", 'POST'])
def project():
    if request.method == 'POST':
        # 如果form表单里没有username这个Key值的话会抛出异常
        username = request.form['username']
        password = request.form['password']
    else:
        # http://127.0.0.1:5000/project/?username=ling
        # 如果前端是用?拼接参数的话,就需要使用args来获取值
        username = request.args['username']
        password = request.args['password']

    return render_template('project.html')


# 使用正则表达式来判断路径正确性
@app.route('/user/<regex("[a-z]{3}"):userid>')
def getUserInfo(userid):
    return '您的用户ID为:' + userid


# 两个路由定向到同一个文件
@app.route('/regest/')
@app.route('/login/')
def loginAction():
    return render_template('login.html', title='登录')


# 404会调用的方法和文件
@app.errorhandler(404)
def page_not_fount(error):
    return render_template('404.html'), 404


# 文件上传相关方法练习
@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = path.abspath(path.dirname(__file__))
        upload_path = path.join(basepath, 'static/uploads')
        f.save(upload_path, secure_filename(f.filename))
        return redirect(url_for('upload'))
    return render_template('upload.html')


if __name__ == '__main__':
    app.run()
