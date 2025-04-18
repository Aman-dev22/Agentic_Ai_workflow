from fastapi import FastAPI, File, UploadFile, HTTPException
import os
from fastapi.responses import JSONResponse
from docx import Document
import io
import shutil
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()
 
app = FastAPI()
 
 
 
@app.get("/")
async def Hello_world():
 
    """Uses This Api To Check If The Apis Work"""
 
    return "I Am Working Great"
 
 
 
@app.post("/upload/")
async def upload_docx(file: UploadFile = File(...)):
 
    """
    Takes a .docx file as input and returns the text from the document.
    Returns:
        str: The text extracted from the .docx document.
    """
 
    if file.content_type != "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return JSONResponse(content={"error": "Invalid file type"}, status_code=400)
    contents = await file.read()
    document = Document(io.BytesIO(contents))
    doc_text = []
    for paragraph in document.paragraphs:
        doc_text.append(paragraph.text)
    text_content = "\n".join(doc_text)
    text = {"content": "\n".join(doc_text)}
    with open("extracted_text.txt", "w",encoding="utf-8") as f:
        f.write(text_content)
    return text
 


from fastapi.responses import FileResponse

@app.get("/download")
def download_zip():
    """
    Streams back the ZIP file named `generated_project_root.zip`
    from the current working directory.
    """
    zip_path = os.getenv("FOLDER_PATH")
    
    if not os.path.isfile(zip_path):
        raise HTTPException(status_code=404, detail="ZIP file not found.")
    return FileResponse(
        path=zip_path,
        filename="project.zip",
        media_type="application/zip"
    )