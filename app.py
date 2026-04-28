from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize FastAPI
app = FastAPI(
    title="AI Chatbot API",
    version="1.0",
    description="FastAPI + LangChain + OpenAI"
)

# Use OpenAI
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Prompts
essay_prompt = ChatPromptTemplate.from_template(
    "Write a short essay about {topic}"
)

poem_prompt = ChatPromptTemplate.from_template(
    "Write a short poem about {topic}"
)

chat_prompt = ChatPromptTemplate.from_template(
    "Answer this question clearly: {question}"
)

# Routes
add_routes(app, essay_prompt | llm, path="/essay")
add_routes(app, poem_prompt | llm, path="/poem")
add_routes(app, chat_prompt | llm, path="/chat")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8003)