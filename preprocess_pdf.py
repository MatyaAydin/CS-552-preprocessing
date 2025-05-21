from mistralai import Mistral
from keys.MISTRAL_KEY import api_key
from langchain_text_splitters import RecursiveCharacterTextSplitter
import base64


client = Mistral(api_key=api_key)

uploaded_file = client.files.upload(
file = {
    "file_name": "./pdfs/Midterm_Practice_Set_Solutions.pdf",
    "content": open("./pdfs/Midterm_Practice_Set_Solutions.pdf", "rb"),
},
purpose="ocr"

)

file_url = client.files.get_signed_url(file_id=uploaded_file.id)
response = client.ocr.process(
    model = "mistral-ocr-latest",
    document = {"type": "document_url", "document_url": file_url.url},
    include_image_base64 = True
)


def data_uri_to_bytes(data_uri):
    _, encoded = data_uri.split(",", 1)
    return base64.b64decode(encoded)


def export_images(image):
    parsed_image = data_uri_to_bytes(image.image_base64)
    with open(image.id, "wb") as f:
        f.write(parsed_image)

with open("output.md", "w") as f:
    for page in response.pages:
        f.write(page.markdown)
        for image in page.images:
            export_images(image)

