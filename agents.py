import os

from crewai import Agent
from langchain.tools import tool
from langchain_google_genai import GoogleGenerativeAI

from file_tools import FileTools

GOOGLE_API_KEY = "api-key"
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

idea_analyst = Agent(
    role = "Idea Analyst",
    goal = "Comprehensively analyse an idea to prepare bluprints for the article to be written",
    backstory="You are an experienced content analyst, well versed in analysing an idea and preparing a blue-print for it.",
    llm = llm,
    verbose=True
)
writer = Agent(
    role = "Fiction Writer",
    goal = "Write compelling fantasy and sci-fi fictions from the ideas given by the analyst",
    backstory="A renowned fiction-writer with 2 times NYT best-selling author in fiction and sci-fi category.",
    llm=llm,
    verbose=True
)

editor = Agent(
    role= "Content Editor",
    goal = "Edit contents written by writer",
    backstory="You are an experienced  editor with years of experience in editing books and stories.",
    llm = llm,
    tools=[FileTools.write_file],
    verbose=True
)
