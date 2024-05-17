from dotenv import load_dotenv
load_dotenv() ### loading the environment variables
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

### function to load gemini pro vision model
model = genai.GenerativeModel("gemini-pro-vision")

def getGeminiResponse(question, image):
    if question!="":
        response = model.generate_content([question, image])
    else:
        response = model.generate_content(image)
    return response.text


st.set_page_config(page_title="Image Model")
st.header("LARGE IMAGE MODEL APPLICATION")
input = st.text_input("Input: ", key="input")
upload_file = st.file_uploader("Upload the Image: ", type=["jpg","jpeg","png"])
submit = st.button("Enter")

image=""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image", use_column_width = True)

if submit:
    response = getGeminiResponse(input, image)
    st.subheader("Response")
    st.write(response)
