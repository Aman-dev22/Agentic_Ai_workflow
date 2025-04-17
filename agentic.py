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