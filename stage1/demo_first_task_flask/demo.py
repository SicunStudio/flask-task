## -*- coding: utf-8 -*-
"""
    demo_first_task_flask.demo
    ~~~~~~~~~~~~~~

    A brief demo for freshmen @Sicun Studio for first TASK with flask.

    :copyright: (c) 2016 by ZhangMing.
    :license: BSD, see LICENSE_FILE for more details.
"""

from flask import Flask
from flask import url_for, render_template


app = Flask('__name__')

@app.route('/')
def index():
    return "<h1>input urls for pages</h1> like:\n\n\
            <h3>127.0.0.1:5000/step1</h3>\n\n\
            <h3>127.0.0.1:5000/step2</h3>\n\n\
            <h3>127.0.0.1:5000/step3<br>like /step3/dalao/Sicun</h3>"

@app.route('/step1/')
def step1():
    return "Hello, World!"

@app.route('/step2/')
def step2():
	return render_template('step2.html')
@app.route('/step3/')
def tmp_step3():
	return "<h3>Please add <tag>&<username> in url like /step3/dalao/Guo</h3>"
@app.route('/step3/<tag>/<username>/')
def step3(tag, username):
    tag_list = ['xianyu', 'juju', 'dalao', 'datui', 'youtiao', 'mengxin']
	# judge if <tag> in the tag_list above
    for list in tag_list:
        if list == tag:
            return render_template('step3.html',tag = list, username = username, tag_list = tag_list)
    return render_template('step3.html',tag = 'other', username = username, tag_list = tag_list)

if __name__ == '__main__':
    app.run(debug=True)
