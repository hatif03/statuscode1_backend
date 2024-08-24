from flask import Flask, request, jsonify
from firebase import get_image_url
import json

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file.filename != 'farhan_ecg.csv':
        return jsonify({'error': 'File not proper'}), 400


@app.route('/get-data', methods=['GET'])
def get_image_data():
    # Example data; in a real scenario, this might come from a database or other source
    f=open('data.json')
    image_data = json.load(f)

    # Add the image URLs to the data
    for item in image_data:
        item['image_url'] = get_image_url(item['ecg/image_name'])

    return jsonify(image_data)

if __name__ == '__main__':
    app.run(debug=True)