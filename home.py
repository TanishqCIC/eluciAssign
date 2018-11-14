from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import os
import pandas as pd
import backpy as bp
import json
import roundy
import meany

UPLOAD_FOLDER = 'f:/eluciAssign/uploads'
#declaring the locationn of upload folder

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#path to upload folder

@app.route('/')
def index():
	return render_template('operations.html')
#if no route is present on call return operations.html

#/upload route uploads attached file
@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	if request.method != ('POST'):
		return 'wrong method called, Only calls on POST are allowed'

	if 'file' not in request.files:
		return "no file"
	else:
		f = request.files['file']
		filename = (secure_filename(f.filename))
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return "file uploaded"

#subdatasets route creates or returns excel file with 3 sheets - PC_DataFrame, LPC_DataFrame and plasmalogen_DataFrame
@app.route('/subdatasets', methods = ['GET', 'POST'])
def subdatasets():
	if request.method != ('POST'):
		return 'wrong method called, Only calls on POST are allowed'
	if not (request.form):
		return 'trivial entry, please enter file name'

	filename = request.form['filename']
	fileLoc = UPLOAD_FOLDER+'/'+filename
	bp.core(fileLoc)
	return send_file('f:/eluciAssign/PythonExport.xlsx')

#/round route rounds off retention time
@app.route('/round', methods = ['GET', 'POST'])
def round():
	if request.method != ('POST'):
		return 'wrong method called, Only calls on POST are allowed'
	if not (request.form):
		return 'trivial entry, please enter file name'
		
	filename = request.form['filename']
	fileLoc = UPLOAD_FOLDER+'/'+filename
	pc = roundy.core(fileLoc)
	return send_file('f:/eluciAssign/PythonExport.xlsx')

#/mean route calculates mean
@app.route('/mean', methods = ['GET', 'POST'])
def mean():
	if request.method != ('POST'):
		return 'wrong method called, Only calls on POST are allowed'
	if not (request.form):
		return 'trivial entry, please enter file name'
		
	filename = request.form['filename']
	fileLoc = UPLOAD_FOLDER+'/'+filename
	pc = meany.core(fileLoc)
	return send_file('f:/eluciAssign/PythonExport.xlsx')

@app.route('/<generic>')
def genric(generic):
	return '[404]  wrong path -- url not found'

if __name__ == "__main__":
	app.run(debug=True)
