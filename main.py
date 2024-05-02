import os
import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# Function to convert user input into message format
def convert_to_message(text):
    return [{"role": "user", "content": text}]

# Function to return the response
def load_answer(question):
    llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), model_name="gpt-3.5-turbo", temperature=0)
    answer = llm.invoke(question)
    return answer.content

# App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("WobsGPT")

# Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

user_input = get_text()

submit = st.button('Generate')

# If generate button is clicked
if submit:
    st.subheader("Answer:")
    message = convert_to_message(user_input)
    response = load_answer(message)
    st.write(response)
