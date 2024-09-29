# CV Analyzer Flask Application

This Flask web application allows users to upload CV documents (PDF or Word format) and extract relevant information from them. The application uses a custom extractor to analyze the content and present the results in a user-friendly interface.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)

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

2. **Create a Conda environment:**
   Open your terminal and run:
   ```bash
   conda create --name cv_analyzer python=3.12
   conda activate cv_analyzer

3. **Install the required packages:**
   Make sure you have requirements.txt in the root of your project. Install the dependencies by running::
   ```bash
   pip install -r requirements.txt

3. **Run the application:**
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

