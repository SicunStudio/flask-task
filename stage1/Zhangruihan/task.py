from flask import Flask,render_template
app = Flask(__name__)

@app.route('/step1')
def step1():
    return 'Hello, World!'
    
@app.route('/step2')
def step2():
    return render_template('hello_world.html')
    
@app.route('/step3/<title>/<name>')
def step3(title,name):
    list=['萌新','油条','大腿','dalao','juju','咸鱼']
    for tag in list:
        if tag==title:
            return render_template('step3.html',title=tag,name=name,list=list)
    return render_template('step3.html',title='other',name=name,list=list)
    