```md
# AI-Powered Chatbot using FastAPI and LangChain

## Overview
This project is an AI chatbot application that generates responses to user queries using Large Language Models (LLMs). It combines a FastAPI-based backend with a simple Streamlit frontend to create an interactive system for real-time text generation.

The goal of this project was to understand how modern AI systems integrate APIs with language models to build practical applications.

---

## Features
- REST API built using FastAPI to handle user queries
- LLM-based response generation using LangChain
- Interactive frontend using Streamlit
- Modular prompt handling for different tasks (essay and poem generation)
- Support for multiple LLM providers (OpenAI, Groq, or local models via Ollama)

---

## Tech Stack
- Python  
- FastAPI  
- LangChain  
- Streamlit  
- OpenAI API / Groq API / Ollama (optional)

---

## Project Structure
```

.
├── app.py          # FastAPI backend
├── client.py       # Streamlit frontend
├── requirements.txt
├── .env            # API keys (not committed)

````

---

## How It Works
1. User enters a query through the Streamlit interface  
2. The request is sent to the FastAPI backend  
3. LangChain processes the prompt and interacts with the LLM  
4. The generated response is returned and displayed to the user  

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-powered-chatbot.git
cd ai-powered-chatbot
````

---

### 2. Install dependencies

```bash
pip install fastapi langchain langchain-openai langchain-groq langchain-community uvicorn streamlit python-dotenv
```

---

### 3. Configure environment variables

Create a `.env` file in the root directory and add your API keys:

```
OPENAI_API_KEY=your_api_key
GROQ_API_KEY=your_api_key
```

---

### 4. Run the FastAPI backend

```bash
python app.py
```

The API will run on:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 5. Run the Streamlit frontend

```bash
streamlit run client.py
```

The app will open in your browser.

---

## Usage

* Select the type of content (essay or poem)
* Enter a topic or query
* Submit the request
* View the generated response in real time

---

## Learning Outcomes

* Built REST APIs using FastAPI
* Integrated LLMs into backend systems using LangChain
* Understood prompt design and response generation
* Learned how frontend and backend interact in AI applications

---

## Future Improvements

* Add document-based retrieval (RAG)
* Implement chat history and memory
* Improve prompt engineering for better responses
* Deploy the application on a cloud platform

---

## Disclaimer

This project is for learning purposes and demonstrates basic integration of LLMs with web frameworks.

