import streamlit as st


with st.sidebar:
    st.selectbox("Select a file", ["file1", "file2", "file3"])
    st.button("Run")


st.header("1. HuggingFace")
st.code("""
import requests

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-small"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("sample1.flac")
""", language="python")

