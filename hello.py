from flask import Flask
from flask import render_template
from flask import send_from_directory
from random import randint
app = Flask(
    __name__, 
    static_url_path='/static')

# url_for('static', filename='style.css')

@app.route("/")
def index():
    return render_template('index.html')

# Other static resources
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)
@app.route('/vendor/<path:path>')
def send_vendor(path):
    return send_from_directory('static/vendor', path)
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)

# Blog post resources
@app.route("/post/<postname>/")
def post1(postname):
    return render_template(postname)
