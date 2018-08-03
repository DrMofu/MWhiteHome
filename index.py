# -*- coding: UTF-8 -*-

from flask import Flask,request,session,redirect,url_for,render_template,g,flash
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/details/')
def details():
	return render_template('details.html')	

@app.route('/test/')
def test():
	return render_template('3Blue1Brown.html')	

if __name__ == '__main__':
	app.run()