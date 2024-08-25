from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from firebase import get_image_url
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()

@app.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file.filename != 'farhan_ecg.csv':
        return jsonify({'error': 'File not proper'}), 400


@app.route('/get-data', methods=['GET', 'POST'])
def get_image_data():
    # Example data; in a real scenario, this might come from a database or other source
    f=open('data.json')
    data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)