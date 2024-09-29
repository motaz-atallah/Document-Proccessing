# app/routes.py

"""
This module defines the routes for the Flask application.

The application allows users to upload PDF and DOCX files for processing using different extractors.
The two available extractors are:
- Google Generative AI
- GPT4All (Meta Llama)

Dependencies:
- Flask: A micro web framework for Python.
- werkzeug: A library for WSGI utilities that includes file handling utilities.
- Extractor modules for processing documents:
  - extractor_google: For Google Generative AI extraction.
  - extractor_gpt4all: For GPT4All extraction.

Constants:
- UPLOAD_FOLDER: The directory where uploaded files are stored.
- ALLOWED_EXTENSIONS: The set of file extensions allowed for upload.

Blueprint:
- A Flask Blueprint is created for organizing routes related to the main application functionalities.

Functions:
- allowed_file(filename): Checks if the uploaded file has an allowed extension.

Routes:
1. GET /:
   - Renders the main HTML page where users can upload documents.

2. POST /upload:
   - Handles file uploads.
   - Validates the uploaded file and the selected extractor type.
   - Saves the file to the UPLOAD_FOLDER.
   - Processes the document using the selected extractor.
   - Returns the extracted information as a JSON response or an error message.
"""

from flask import Blueprint, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from app.extractors.extractor_google import extract_information as extract_information_google
from app.extractors.extractor_gpt4all import extract_information as extract_information_gpt4all

UPLOAD_FOLDER = './uploads'  # Directory for uploaded files
ALLOWED_EXTENSIONS = {'pdf', 'docx'}  # Allowed file types for upload

# Create a Blueprint for the routes
main = Blueprint('main', __name__)

# Ensure the 'uploads' folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the filename has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def index():
    """Render the main HTML page for file upload."""
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    """Handle the file upload and document processing.

    Returns:
        JSON response containing the extracted information or an error message.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    extractor_type = request.form.get('extractor')  # Get the extractor type from the form

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)  # Save the file

        # Process the document based on the selected extractor
        try:
            if extractor_type == 'generativeai':
                result = extract_information_google(filepath)
            elif extractor_type == 'metamodel':
                result = extract_information_gpt4all(filepath)
            else:
                return jsonify({'error': 'Invalid extractor type selected.'}), 400
            
            if not result:
                return jsonify({'error': 'No result returned from document processing.'}), 500
            
            return jsonify({'result': result}), 200
        except Exception as e:
            return jsonify({'error': f'Error processing file: {e}'}), 500
    else:
        return jsonify({'error': 'Allowed file types are pdf, docx'}), 400
