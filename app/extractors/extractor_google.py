import google.generativeai as genai
from app.utils.document_utils import process_document
from config import Config

# Configure the Google Generative AI API with the provided API key
genai.configure(api_key=Config.API_KEY)

def extract_information(file_path):
    """
    Extracts relevant information from a document.

    This function processes the document located at `file_path`, 
    sends the extracted text to a generative AI model to extract 
    personal information, education details, and work experience, 
    and returns the formatted output as an HTML snippet.

    Parameters:
    - file_path (str): The path to the document file from which 
      information will be extracted. The document is expected to 
      contain structured information such as personal details, 
      educational background, and work history.

    Returns:
    - str: A string containing the extracted information formatted 
      as an HTML snippet with predefined Bootstrap classes.

    Raises:
    - ValueError: If the response from the generative AI model 
      is empty after processing the document.
    """
    text = process_document(file_path)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = f"""
    Please extract the following details from the document text: {text}
    1. Personal Information (Name, Gender, Age)
    2. Education (Degree, Institution, GPA, Start Date, End Date)
    3. Work Experience (Company, Role, Location, Start Date, End Date, Description)

    Please format the output as an HTML snippet using predefined Bootstrap classes. The output should only include the extracted information, without any additional text or context.
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
    extracted_info = extract_information(file_path)
