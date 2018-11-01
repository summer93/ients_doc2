from flask import Flask, make_response, send_file,request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
arg = True

@app.route('/static/<filename>')
def upload_file(filename):
    if arg:
    	return send_file('/data/{}'.format(filename))
    else:
        return 'no!no!no!'


if __name__ == '__main__':
    app.run(debug=True)
