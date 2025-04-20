from mistralai import Mistral
from MISTRAL_KEY import api_key


client = Mistral(api_key=api_key)

pdf_name = "./pdfs/mcq_simple.pdf"


uploaded_pdf = client.files.upload(
    file={
        "file_name": pdf_name,
        "content": open(pdf_name, "rb"),
    },
    purpose="ocr"
)  


file_url = client.files.get_signed_url(file_id=uploaded_pdf.id)


response = client.ocr.process(
    model = "mistral-ocr-latest",
    document = {"type": "document_url", "document_url": file_url.url},
    include_image_base64 = True
)




def parse_qa_string(input_string, question_number):
    current_marker = f'Question {question_number}'
    next_marker = f'Question {question_number + 1}'
    
    start_idx = input_string.find(current_marker)
    end_idx = input_string.find(next_marker)
    
    if start_idx == -1:
        raise ValueError(f"Could not find '{current_marker}' in the input.")
    
    # Slice between current and next question (or end of string)
    if end_idx != -1:
        question_block = input_string[start_idx:end_idx]
    else:
        question_block = input_string[start_idx:]
    
    # Remove the "Question X" prefix
    question_block = question_block.split(' ', 2)[-1]
    
    # Split into question and solution
    if 'Solution:' in question_block:
        question_part, solution_part = question_block.split('Solution:', 1)
        question = question_part.strip()
        solution = solution_part.strip()
        return {
            "question": question,
            "solution": solution
        }
    else:
        raise ValueError("Input string does not contain 'Solution:' keyword.")

    
qa = parse_qa_string(response.pages[0].markdown, 1)

print("###QUESTION###")
print(qa['question'])
print("###SOLUTION###")
print(qa['solution'])
