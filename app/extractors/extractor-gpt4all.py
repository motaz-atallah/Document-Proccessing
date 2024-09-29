from gpt4all import GPT4All

from app.utils.document_utils import process_document

def extract_information(file_path):
    text = process_document(file_path)
    model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

    prompt = f"""
        Please extract the following details:
            1. Personal Information (Name, Gender, Age)
            2. Education (Degree, Institution, GPA, Start Date, End Date)
            3. Work Experience (Company, Role, Location, Start Date, End Date, Description)
            from the document text: {text}
        """
    return model.generate(prompt)

if __name__ == "__main__":
    file_path = "Your-PDF.pdf"  # Change to your actual CV path
    extracted_info = extract_information(file_path)
