import streamlit as st
import http.client
import json

# Function to communicate with the ChatGPT API
def get_chatbot_response(user_input):
    conn = http.client.HTTPSConnection("chat-gpt26.p.rapidapi.com")
    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_input}]
    })
    headers = {
        'x-rapidapi-key': "10b8ea539emsh303325ea16a546ep175db6jsn340dbef4f66a",
        'x-rapidapi-host': "chat-gpt26.p.rapidapi.com",
        'Content-Type': "application/json"
    }
    conn.request("POST", "/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

# Streamlit app layout
st.set_page_config(page_title="ChatGPT 3.5 Turbo Chatbot", layout="centered")
st.title("ChatGPT 3.5 Turbo Chatbot")

# User input
user_input = st.text_input("You: ", "")

if user_input:
    response = get_chatbot_response(user_input)
    chatbot_reply = response['choices'][0]['message']['content']
    st.write(f"Chatbot: {chatbot_reply}")

# Custom CSS
st.markdown("""
    <style>
    .stTextInput input {
        background-color: #fff;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton button {
        background-color: #E64A19;
        color: #fff;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Custom JavaScript (if needed)
st.components.v1.html("""
    <script>
    // Custom JavaScript code here
    </script>
""")
