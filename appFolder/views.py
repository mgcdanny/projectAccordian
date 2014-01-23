from flask import make_response, request, jsonify, Response 
from appFolder import app, testP

@app.route('/')
def ui(page=None):
	return make_response(open('appFolder/index.html').read())

@app.route('/api/project')
def test():
	return jsonify(data=testP)

