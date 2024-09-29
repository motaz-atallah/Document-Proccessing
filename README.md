# CV Analyzer Flask Application

This Flask web application allows users to upload CV documents (PDF or Word format) and extract relevant information from them. The application uses a custom extractor to analyze the content and present the results in a user-friendly interface.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Folder Structure](#folder-structure)
- [License](#license)

## Features

- **File Upload**: Users can upload PDF or Word CV documents for analysis.
- **Information Extraction**: Extracts relevant data such as skills, experience, education, and contact details from CVs.
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