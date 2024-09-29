from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from extractor_google import extract_information

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret_key"

# Ensure the 'uploads' folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_container')
def upload_container():
    return render_template('upload_container.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Process the document and return the result
        try:
            result = extract_information(filepath)
            if not result:
                return jsonify({'error': 'No result returned from document processing.'}), 500
            return jsonify({'result': result}), 200
        except Exception as e:
            return jsonify({'error': f'Error processing file: {e}'}), 500
    else:
        return jsonify({'error': 'Allowed file types are pdf, docx'}), 400

if __name__ == "__main__":
    app.run(debug=True)
