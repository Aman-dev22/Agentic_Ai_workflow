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