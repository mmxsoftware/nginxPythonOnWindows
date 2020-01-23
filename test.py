# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

#以下是WEB Server
app = Flask(__name__)

@app.route('/api') 
def hello_world(): 
	return 'Hello World!'

@app.route('/api/new') 
def hello_new_world(): 
	return 'Hello New World!'

if __name__ == '__main__':
	print("啟動WEB服務")
	app.run(port=8000)
	print("WEB Server已停止.")