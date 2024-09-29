# CV Analyzer Flask Application

This Flask web application allows users to upload CV documents (PDF or Word format) and extract relevant information from them. The application uses a custom extractor to analyze the content and present the results in a user-friendly interface.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Challenges](#Challenges)
- [ArchitectureDesign](#ArchitectureDesign)

## Features

- **File Upload**: Users can upload PDF or Word CV documents for analysis.
- **Information Extraction**: Extracts relevant data such as skills, experience, education, and contact details from CVs.
- **Data Extraction Options**: Choose between:
  - **Google Generative AI**: Leverage the power of Google's AI to extract information.
  - **gpt4all Meta-Llama-3-8B-Instruct Model**: Use the open-source Llama model for data extraction.
- **User Interface**: Built with Bootstrap for a responsive and modern design.
- **Error Handling**: Displays appropriate error messages for unsupported file types or processing errors.

## Installation

Follow these steps to set up the application on your local machine:

1. **Clone the repository:**
   Open your terminal and run:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Create a environment:**
   You can choose one of the following options to create a Python environment for the application:

   #### Option 1: Using Conda

   If you prefer using Conda, follow these steps:

   ```bash
   conda create --name cv_analyzer python=3.12
   conda activate cv_analyzer
   ```

   #### Option 2: Using venv

   If you prefer using Python's built-in venv, follow these steps:

   ```bash
   python -m venv cv_analyzer_env
   source cv_analyzer_env/bin/activate  # For Linux/macOS
   cv_analyzer_env\Scripts\activate      # For Windows
   ```

3. **Install the required packages:**
   Make sure you have requirements.txt in the root of your project. Install the dependencies by running::
   ```bash
   pip install -r requirements.txt

3. **Run the application:** (make sure to check the [Configuration](#configuration) section before you run the app)
    ```bash
    python -m app.run

## Configuration

### Data Extraction Options

You can choose between two methods for data extraction in the application:

1. **Using Google Generative AI**:
   - To use Google Generative AI, you'll need to obtain a free API key. Follow these steps:
     - Visit the [Google Cloud Console](https://console.cloud.google.com/).
     - Create a new project or select an existing one from the list.
     - Navigate to the "APIs & Services" section and enable the "Google Generative AI API".
     - Go to the "Credentials" tab and click "Create Credentials".
     - Choose "API Key", and your key will be generated. Copy this key (You can edit the key from the list below to restricted for Generative Language API).
     - Inside the config.py make sure to replace the value

2. **Using gpt4all Meta-Llama-3-8B-Instruct Model**:
   - The application supports the use of the **GPT4All Python SDK** to run large language models (LLMs) locally for CV data extraction. One of the supported models is the **Meta-Llama-3-8B-Instruct.Q4_0.gguf** model, which allows users to leverage advanced language models without relying on external cloud services.
   - **Automatic Model Download**: When selecting the GPT4ALL model in the application for the first time, the model will automatically be downloaded (approximately 4.66GB in size) and stored locally.
   - **Model Setup**: Once the model is downloaded, the application will use it for processing all subsequent CV uploads.
   - Ensure that you have sufficient disk space and a stable internet connection for the model download.

This provides an efficient, offline alternative to cloud-based AI services, ensuring your data stays private and secure on your local system.

## Challenges

- **Model Selection**: Initially faced challenges in selecting the right AI model for optimal performance. The decision to use gpt4all and Google Generative AI involved extensive testing.
- **Document Parsing**: Different CV formats and layouts led to difficulties in accurately parsing and extracting relevant information.
- **Resource Limitations**: Running AI models locally resulted in slower processing times due to memory and CPU constraints. This limitation prompted the exploration of cloud-based alternatives.
- **Data Privacy**: Ensuring user data privacy when using external APIs was a significant consideration.


## ArchitectureDesign
The architecture of the CV Analyzer Flask Application is designed to facilitate the seamless upload, processing, and extraction of information from CV documents. Below are the key components of the architecture:

- **Client Layer**: Web Interface: The client layer consists of a responsive web interface built using HTML, CSS, and Bootstrap. This layer provides users with the ability to upload their CVs, select the extraction method, and view the results in a user-friendly format.
- **Application Layer**: 
   - **Flask Application**: The core of the application is built using Flask, a lightweight Python web framework. This layer handles HTTP requests, manages user sessions, and serves the web pages.
   - **File Upload Handler**: This component is responsible for handling incoming file uploads, ensuring that the files are in the correct format (PDF or Word) and storing them temporarily for processing.
- **Extraction Layer**: Running AI models locally resulted in slower processing times due to memory and CPU constraints. This limitation prompted the exploration of cloud-based alternatives.
- **Data Extraction Options**: The application offers two data extraction methods:
   - **Google Generative AI**: This component interacts with the Google Generative AI API to extract relevant information from the uploaded CVs. It requires an API key for authentication and processes the document content through the API.
   - **gpt4all Meta-Llama-3-8B-Instruct Model**: This component uses the GPT4All Python SDK to load the local LLM model for CV data extraction. The model is downloaded and stored locally, allowing for offline processing of CVs without external dependencies.
- **Processing Layer**: 
   - **Document Parsing**: This component utilizes libraries such as PyPDF2 for PDF parsing and python-docx for Word document parsing. It extracts raw text from the documents, which is then fed into the chosen extraction model for analysis.
   - **Information Structuring**: After extraction, the relevant information (such as personal details, education, and work experience) is structured into a predefined format, ready for display.
- **Storage Layer**: 
   - **Temporary Storage**: Uploaded documents are temporarily stored in a designated directory on the server. This ensures that files can be accessed for processing and removed after the extraction is complete.
   - **Configuration File:**: The application uses a configuration file (config.py) to store sensitive information, such as API keys and model paths, ensuring secure management of credentials
- **User Interface Layer**: 
   - **Result Display**:  After processing, the extracted information is displayed on the user interface in a structured and readable format, allowing users to review the data. Bootstrap is used to enhance the presentation of results.
   
### Architectural Diagram
Here’s a simple textual representation of how the components relate:

+---------------------+
|      Client Layer   |
| (Web Interface)     |
+---------------------+
            |
            v
+---------------------+
|   Application Layer  |
|   (Flask App)       |
+---------------------+
            |
            v
+---------------------+          +----------------------+
|  Extraction Layer   | <------>|  Google Generative AI |
| (Data Extraction)   |          |  (API Interaction)   |
|                     |          +----------------------+
|                     |          
|                     |          +----------------------+
|                     | <------>|  gpt4all Model       |
|                     |          |  (Local Processing)  |
+---------------------+          +----------------------+
            |
            v
+---------------------+
|   Processing Layer   |
| (Document Parsing &  |
|  Information Struct.)|
+---------------------+
            |
            v
+---------------------+
|   Storage Layer      |
| (Temporary Storage)  |
+---------------------+
            |
            v
+---------------------+
| User Interface Layer |
| (Result Display)     |
+---------------------+
