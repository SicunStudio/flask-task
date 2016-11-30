from flask import Flask,render_template
app=Flask(__name__)


@app.route('/step1')
def hello_world1():
    return 'Hello World!'
@app.route('/step2')
def hello_world2():
    return render_template('hello_world2.html')
@app.route('/step3/<tag>/<name>/')
def hello(tag, name):
    tag_list = ['xianyu', 'juju', 'dalao', 'datui', 'youtiao', 'mengxin']
    for list in tag_list:
        if list == tag:
            return render_template('hello.html',tag = list, name = name, tag_list = tag_list)
    return render_template('hello.html',tag = 'other', name = name, tag_list = tag_list)

if __name__=='__main__':
    app.run()