from gpt4all import GPT4All
from app.utils.document_utils import process_document

def extract_information(file_path):
    """
    Extracts structured information from a CV document.

    This function processes the document located at `file_path`, 
    sends the extracted text to the GPT-4All model to retrieve 
    personal information, education details, and work experience, 
    and returns the formatted output as an HTML snippet.

    Parameters:
    - file_path (str): The path to the document file from which 
      information will be extracted. The document is expected to 
      contain structured information such as personal details, 
      educational background, and work history.

    Returns:
    - str: A string containing the extracted information formatted 
      as an HTML snippet with Bootstrap classes.

    Raises:
    - ValueError: If the response from the generative model is empty 
      after processing the document.
    """
    
    # Process the document to extract text
    text = process_document(file_path)

    # Initialize the GPT4All model
    model = GPT4All(
        "Meta-Llama-3-8B-Instruct.Q4_0.gguf",
        device="cpu",
        n_ctx=2048,
        ngl=4
    )

    # Start a chat session
    with model.chat_session() as chat:
        queries = {
            "Personal Information": "Extract Name, Gender, and Age from the document text. Format the output as an HTML snippet using Bootstrap.",
            "Education": "Extract all instances of Degree, Institution, GPA, Start Date, and End Date from the document text. Format the output as an HTML snippet using Bootstrap classes, ensuring that multiple entries are captured appropriately.",
            "Work Experience": "Extract all instances of Company, Role, Location, Start Date, End Date, and Description from the document text. Format the output as an HTML snippet using Bootstrap classes, ensuring that multiple entries are captured appropriately."
        }

        extracted_data = {}

        # Iterate over the queries to get responses from the model
        for category, query in queries.items():
            prompt = f"{query} Based on the document text: {text}"
            response = chat.generate(prompt)
            extracted_data[category] = response.strip()

    # Combine all extracted HTML snippets into one output
    html_output = f"""
    {extracted_data.get("Personal Information", "<p>No data found.</p>")}
    {extracted_data.get("Education", "<p>No data found.</p>")}
    {extracted_data.get("Work Experience", "<p>No data found.</p>")}
    """
    return html_output

if __name__ == "__main__":
    file_path = "Your-PDF.pdf"  # Change to your actual CV path
    extracted_info = extract_information(file_path)
