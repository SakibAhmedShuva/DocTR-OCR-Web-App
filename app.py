import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import numpy as np
from PIL import Image
import io

# Set the environment variable to use the TensorFlow backend
os.environ["USE_TF"] = "1"

app = Flask(__name__)
# Enable CORS for all routes and origins
CORS(app)

# Load the OCR model once when the application starts
print("Loading OCR model...")
model = ocr_predictor(pretrained=True)
print("Model loaded successfully.")

@app.route('/', methods=['GET'])
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/ocr', methods=['POST'])
def perform_ocr():
    """Handles image uploads and performs OCR."""
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files part in the request'}), 400

    files = request.files.getlist('files[]')
    if not files or all(f.filename == '' for f in files):
        return jsonify({'error': 'No selected files'}), 400

    results = []
    for file in files:
        try:
            # Read the image file from the request
            img_bytes = file.read()
            # Create a document from the image bytes
            doc = DocumentFile.from_images([img_bytes])
            
            # Perform OCR
            result = model(doc)
            output = result.export()

            # Extract text and confidence scores
            lines = []
            for page in output['pages']:
                for block in page['blocks']:
                    for line in block['lines']:
                        line_text = " ".join([word['value'] for word in line['words']])
                        confidence = sum(word['confidence'] for word in line['words']) / (len(line['words']) or 1)
                        lines.append({
                            'text': line_text,
                            'confidence': float(f"{confidence:.2f}")
                        })
            
            results.append({
                'filename': file.filename,
                'lines': lines
            })

        except Exception as e:
            results.append({
                'filename': file.filename,
                'error': str(e)
            })
            
    return jsonify(results)

if __name__ == '__main__':
    # Running on 0.0.0.0 makes it accessible on your local network
    app.run(host='0.0.0.0', port=5000, debug=True)