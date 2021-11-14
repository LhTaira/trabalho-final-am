import flask
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import json
import os

import segmentation

UPLOAD_FOLDER = './files/'

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def hello():
    if 'file' in request.files:
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        resposta = segmentation.faz_tudo(file.filename)
        os.remove('./files/'+ file.filename)



    return 'Success', 200

if __name__ == '__main__':
    app.run()