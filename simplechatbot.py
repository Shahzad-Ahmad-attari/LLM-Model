from dotenv import load_dotenv # type: ignore
load_dotenv() # loading all the environment variables

import streamlit as st # type: ignore
import os 

import google.generativeai as genai # type: ignore

genai.configure(api_key=os.getenv("Google_API_KEY"))

## function to load Gemini pro modle and get responses
 
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
     response = model.generate_content(question)
     return response.text

#initilaize our streamlit app

st.set_page_config(page_title="Gemini lec 3(a)")

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

# when submit is clicked

if submit:
   response=get_gemini_response(input)
   st.subheader("The response is")
   st.write(response)
 