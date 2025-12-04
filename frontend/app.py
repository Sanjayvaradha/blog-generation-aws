import streamlit as st
import requests
import json

API_URL = "https://0vzwi7rxck.execute-api.us-east-1.amazonaws.com/development/blog-generation"
API_KEY = "<your-api-key>"

st.title("AI Blog Generator")

blog_topic = st.text_input("Enter a blog topic:")

if st.button("Generate Blog"):
    if blog_topic.strip() == "":
        st.error("Please enter a topic.")
    else:
        headers = {
            "x-api-key": API_KEY,
            "Content-Type": "application/json"
        }
        payload = {"blogtopic": blog_topic}

        with st.spinner("Generating blog..."):
            response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            st.success("Blog generated successfully!")
            st.write(response.json())
        else:
            st.error(f"Error: {response.status_code}")
            st.write(response.text)
