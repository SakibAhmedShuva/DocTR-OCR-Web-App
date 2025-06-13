# DocTR OCR Web Application

A robust and user-friendly web application for performing Optical Character Recognition (OCR) on multiple images simultaneously. Built with the powerful DocTR library and TensorFlow backend, served through a lightweight Flask web server.

![image](https://github.com/user-attachments/assets/6c5c54b3-1530-42b7-8584-094503570c0d)

## ✨ Features

- **🔄 Bulk Image Processing**: Upload and process multiple images simultaneously
- **🎨 Intuitive Web Interface**: Clean, modern, and easy-to-use interface
- **📊 Confidence Scores**: View model confidence levels for each extracted text line
- **🔒 Stable Dependencies**: Pinned library versions ensure consistent performance
- **🚀 RESTful API**: Programmatic access via `/ocr` endpoint
- **⚡ Fast Processing**: Optimized for quick OCR operations

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python, Flask |
| **OCR Engine** | DocTR (python-doctr) |
| **Deep Learning** | TensorFlow |
| **Frontend** | HTML5, CSS3, JavaScript (Fetch API) |

## 📋 Prerequisites

- **Python**: Version 3.9 - 3.11 (recommended)
- **Git**: For repository cloning
- **Virtual Environment**: Recommended for dependency isolation

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/SakibAhmedShuva/DocTR-OCR-Web-App.git
cd DocTR-OCR-Web-App
```

### 2. Set Up Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> **Note**: After activation, you should see `(venv)` at the beginning of your command prompt.

### 3. Install Dependencies

Create a `requirements.txt` file in the project root with the following content:

```txt
Flask
Flask-Cors
tensorflow==2.15.0
python-doctr[tf]==0.7.0
gunicorn
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

> **Important**: We use pinned versions (TensorFlow 2.15.0, DocTR 0.7.0) to ensure stability and avoid compatibility issues.

### 4. Run the Application

```bash
python app.py
```

The server will start and display:
```
* Serving Flask app 'app'
* Running on http://127.0.0.1:5000
```

### 5. Access the Application

1. Open your web browser
2. Navigate to `http://127.0.0.1:5000`
3. Click "Select Images" to choose your image files
4. Click "Upload and Process" to perform OCR

## 🔧 API Usage

The application provides a RESTful API endpoint for programmatic access:

### POST `/ocr`

Upload images and receive OCR results in JSON format.

**Example Request:**
```bash
curl -X POST -F "file=@image.jpg" http://127.0.0.1:5000/ocr
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### ❌ ValueError: Layer expected 1 variables, but received 0 variables

**Cause**: Corrupted or mismatched model weights, often from interrupted downloads.

**Solution**:
1. Stop the Flask server (`Ctrl+C`)
2. Delete the DocTR cache folder:
   - **Windows**: `C:\Users\<YourUsername>\.cache\doctr`
   - **macOS/Linux**: `~/.cache\doctr`
3. Restart with `python app.py` (DocTR will re-download fresh models)

#### ❌ ModuleNotFoundError or AttributeError

**Cause**: Python environment or dependency issues.

**Solution**:
1. Verify virtual environment is activated (look for `(venv)` in terminal)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Ensure Python version compatibility (3.9-3.11)

#### ❌ Memory Issues

**Cause**: Processing large images or multiple files simultaneously.

**Solution**:
- Reduce image size before processing
- Process fewer images at once
- Increase system RAM if possible

## 📁 Project Structure

```
DocTR-OCR-Web-App/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
├── static/              # CSS, JS, and static assets
└── README.md           # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [DocTR](https://github.com/mindee/doctr) - Powerful OCR library
- [TensorFlow](https://tensorflow.org/) - Machine learning framework
- [Flask](https://flask.palletsprojects.com/) - Web framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review existing [GitHub Issues](https://github.com/SakibAhmedShuva/DocTR-OCR-Web-App/issues)
3. Create a new issue with detailed information about your problem

---

**Made with ❤️ by [SakibAhmedShuva](https://github.com/SakibAhmedShuva)**
