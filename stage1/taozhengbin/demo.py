#!/usr/bin/env python3
from flask import Flask,render_template

app = Flask(__name__)

nickname=['咸鱼','juju','dalao','大腿','油条','萌新']

@app.route('/step1/')
def step1():
    return 'Hello World'

@app.route('/step2/')
def step2():
   return render_template('step2.html') 

@app.route('/step3/<name>/<address>/')
def step3(name,address):
        return render_template('content.html',name=name,address=address,nickname=nickname)

if __name__ == '__main__':
    app.run(debug= True)
