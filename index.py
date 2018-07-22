# -*- coding: UTF-8 -*-

from flask import Flask,request,session,redirect,url_for,render_template,g,flash
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
	return 'index'