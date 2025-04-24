from mistralai import Mistral
from keys.MISTRAL_KEY import api_key
import pandas as pd


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




def parse_qa_string(input_string):
    result = {"questions": [], "solutions": []}
    question_number = 1
    
    while True:
        current_marker = f'Question {question_number}'
        next_marker = f'Question {question_number + 1}'
        
        start_idx = input_string.find(current_marker)
        if start_idx == -1:
            break
        
        end_idx = input_string.find(next_marker)
        if end_idx != -1:
            question_block = input_string[start_idx:end_idx]
        else:
            question_block = input_string[start_idx:]


        question_block = question_block.split(' ', 2)[-1] 
        
        if 'Solution:' in question_block:
            question_part, solution_part = question_block.split('Solution:', 1)
            question = question_part.strip()
            solution = solution_part.strip()

            result["questions"].append(question)
            result["solutions"].append(solution)
            
        else:
            raise ValueError(f"Question {question_number} does not contain 'Solution:' keyword.")
        
        question_number += 1
    
    return result



qa = parse_qa_string(response.pages[0].markdown)
df = pd.DataFrame(qa)
df.to_csv("mcq.csv", index=False)


