from crewai_tools import SerperDevTool
import os

search_tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")
