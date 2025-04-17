import os
import subprocess
import json
import re
from typing import TypedDict, Optional, List, Dict
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
 

load_dotenv()
model = ChatGroq(model=os.getenv("MODEL_NAME"), temperature=0, api_key=os.getenv("GROQ_API_KEY"))


from langsmith import utils
from langsmith import traceable
utils.tracing_is_enabled()
 

class FileStructureState(TypedDict):
   
   """A TypedDict representing the state of the file structure generation
   process with attributes: srs_text (str), file_structure (Optional[List[str]]),
   file_descriptions (Optional[Dict[str, str]]), folder_path (str), error_log
   Optional[str]), retry_count (int), code_feedback (Optional[Dict[str, str]]),
   improvement_count (int)."""
   
   srs_text: str
   file_structure: Optional[List[str]]
   file_descriptions: Optional[Dict[str, str]]
   folder_path: str
   error_log: Optional[str]
   retry_count: int
   code_feedback: Optional[Dict[str, str]]
   improvement_count: int



@traceable
def srs_to_file_structure(state: FileStructureState) -> FileStructureState:
 
    """Generates a file structure and descriptions from the SRS document."""
   
    prompt = f"""
    You are a software architect. Given the following SRS document:
    {state["srs_text"]}
    - Generate a structured JSON file tree.
    - Provide a detailed description of each file's purpose and what should be inside it and generate docker file as well and create readme files for every thing and requirements.txt.
    - do not generate tests
    - Return a JSON object with:
      - 'files': List of file paths.
      - 'descriptions': Dictionary mapping file paths to their descriptions. Each description should comprehensively outline the structure and purpose of the file, including: Classes:List all the classes that should be present in the file., Provide a detailed description of what each class should do.,Explain the role and functionality of each class within the context of the file.,Variables: List all the key variables that should be present in the file., Describe the purpose and usage of each variable., Include details on the scope and type of each variable., Methods: List all the methods that should be present in the file. Provide a detailed description of what each method should do., Explain the inputs, outputs, and side effects of each method.
    - Ensure the response is in valid JSON format without any additional text.
    """
   
    response = model.invoke(prompt)
    response_str = response.content
 
    json_match = re.search(r"```json\s+(.*?)\s+```", response_str, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
        json_data = json.loads(json_str)
 
        file_structure = json_data["files"]
        file_descriptions = json_data["descriptions"]
 
        state["file_structure"] = file_structure
        state["file_descriptions"] = file_descriptions
    else:
        print("JSON data not found")
 
    return state