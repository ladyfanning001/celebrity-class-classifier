from flask import Flask, request, jsonify, send_file, render_template
import util
import os

app = Flask(__name__)

@app.route('/images/<filename>')
def serve_image(filename):
    return send_file(os.path.join(os.path.dirname(__file__), 'images', filename))

@app.route('/')
def index():
    html_path = os.path.join(os.path.dirname(__file__), 'celebrity_face_classification.html')
    return send_file(html_path)

@app.route('/Classify_image', methods=['POST'])
def Classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask server for celebrity classification...")
    util.load_saved_artifacts()
    app.run(port=5015, debug=True)