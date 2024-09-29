import google.generativeai as genai
import os

from document_utils import process_document

genai.configure(api_key="AIzaSyBnjHnK9lBu1LMFZTefvKYPA5gETCXffKU")

def extract_information(file_path):
    text = process_document(file_path)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = f"""
    Please extract the following details from the document text: {text}
    1. Personal Information (Name, Gender, Age)
    2. Education (Degree, Institution, GPA, Start Date, End Date)
    3. Work Experience (Company, Role, Location, Start Date, End Date, Description)

    Format the output as an HTML with predefined bootstrap classes and no need for any extrat information
    No need for html, head and body tags
    """
    
    # Call the model for text generation
    response = model.generate_content(prompt)

    # Check if the response is empty
    if not response.text.strip():
        raise ValueError("Response from model is empty.")
    
    cleaned_response = response.text.replace("```html", "").replace("```", "").strip()
    # Return or process the HTML response as needed
    return cleaned_response

if __name__ == "__main__":
    # Replace with your document path
    file_path = "Your-pdf.pdf"  # Change to your actual document path
    extracted_info = extract_information()
