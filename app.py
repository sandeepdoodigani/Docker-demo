# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 17:41:18 2021

@author: SmartBridgePC
"""

from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
	return "welcome to the DevOPS"

@app.route('/admin')
def admin():
	return "welcome to the Admin"


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)
