import os
import base64
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

# It's recommended by doctr to set the backend before importing tensorflow
os.environ["USE_TF"] = "1"

app = Flask(__name__)
# Enable CORS for all routes and origins
CORS(app)

# Load the OCR model once when the application starts
# This can take some time and memory.
print("Loading DocTR OCR model...")
# Using 'fast' for quicker loading and inference, suitable for a web app.
# For higher accuracy, you can use the default `pretrained=True`.
model = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)
print("Model loaded successfully.")

@app.route('/', methods=['GET'])
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/ocr', methods=['POST'])
def perform_ocr():
    """Handles image uploads, performs OCR, and returns results with image data."""
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files part in the request'}), 400

    files = request.files.getlist('files[]')
    if not files or all(f.filename == '' for f in files):
        return jsonify({'error': 'No selected files'}), 400

    results = []
    for file in files:
        try:
            # Read image bytes and create a data URL for the frontend
            img_bytes = file.read()
            b64_img_str = base64.b64encode(img_bytes).decode('utf-8')
            image_data_url = f"data:{file.mimetype};base64,{b64_img_str}"

            # Create a document from the image bytes for OCR
            # Using from_images is more direct than from_pdf for single images
            doc = DocumentFile.from_images([img_bytes])
            
            # Perform OCR
            result = model(doc)
            output = result.export()

            # Extract and format the text
            full_text_lines = []
            for page in output['pages']:
                for block in page['blocks']:
                    for line in block['lines']:
                        line_text = " ".join([word['value'] for word in line['words']])
                        full_text_lines.append(line_text)
            
            full_text = "\n".join(full_text_lines)
            
            results.append({
                'filename': file.filename,
                'status': 'success',
                'text': full_text if full_text else "No text could be detected in this image.",
                'image_data_url': image_data_url
            })

        except Exception as e:
            # If an error occurs, we still send back the image data URL
            # so the frontend can display which image failed.
            if 'image_data_url' not in locals():
                img_bytes = file.read()
                b64_img_str = base64.b64encode(img_bytes).decode('utf-8')
                image_data_url = f"data:{file.mimetype};base64,{b64_img_str}"
                
            results.append({
                'filename': file.filename,
                'status': 'error',
                'error': f"An error occurred during processing: {str(e)}",
                'image_data_url': image_data_url
            })
            
    return jsonify(results)

if __name__ == '__main__':
    # Running on 0.0.0.0 makes it accessible on your local network
    app.run(host='0.0.0.0', port=5000, debug=False) # Debug set to False for production