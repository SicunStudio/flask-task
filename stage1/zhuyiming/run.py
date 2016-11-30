from flask import Flask
from flask import url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "<h1>input urls for pages like</h1>\n\n\
	<h1>127.0.0.1:5000/step1</h1>\n\n\
	<h1>127.0.0.1:5000/step2</h1>\n\n\
	<h1>127.0.0.1:5000/step3/[2]/[1]</h1>"
	
@app.route('/step1/')
def step1():
    return "Hello, World!"

@app.route('/step2/')
def step2():
    return render_template('step2.html')
@app.route('/step3/<tag>/<name>/')
def step3(tag, name):
    taglist = ('xianyu', 'juju', 'dalao', 'datui', 'youtiao', 'mengxin')
    aa = False
    for tmp in taglist:
        if tmp == tag:
            aa = True
    if not aa:
        tag = 'other'
    return render_template('step3.html', tag = tag, username = name, tag_list = taglist)

app.run(debug = True)
