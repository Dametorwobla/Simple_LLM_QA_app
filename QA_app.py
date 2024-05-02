import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(
    api_key=key,
    model_name="gpt-3.5-turbo")

our_query = "What is the currency of Ghana?"
completion = llm.invoke(our_query)

print(completion)