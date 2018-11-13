from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = 'f:/eluciAssign/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	return render_template('operations.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	if 'file' not in request.files:
		return "no file"
	else:
		f = request.files['file']
		f.save(secure_filename(f.filename))
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
		return "file uploaded"



if __name__ == "__main__":
	app.run(debug=True)
