import streamlit as st
import requests
from streamlit_ace import st_ace

# JDoodle API credentials (replace with your actual credentials)
JDoodle_clientId = 'da1586f97ac8d94d052add1c1fbad2d9'
JDoodle_clientSecret = '122a89db5c5230a2fb63903580ac0cc8d7e21b4e2917f89c5feeb5dd6fe65f15'

# Function to run the code using JDoodle API
def run_code(language, code, stdin):
    # Mapping Streamlit language selection to JDoodle parameters
    language_map = {
        "Python": ("python3", "3"),
        "Java": ("java", "4")
    }

    if language not in language_map:
        return "Unsupported language"

    jdoodle_language, version_index = language_map[language]

    url = "https://api.jdoodle.com/v1/execute"
    data = {
        "clientId": JDoodle_clientId,
        "clientSecret": JDoodle_clientSecret,
        "script": code,
        "language": jdoodle_language,
        "versionIndex": version_index,
        "stdin": stdin  # Pass standard input
    }

    response = requests.post(url, json=data)
    result = response.json()
    
    return result.get("output", result.get("error", "Unknown error"))

# Streamlit app layout
st.title("Java and Python Code Compiler")

language = st.selectbox("Select Language", ["Python", "Java"])

# Use streamlit-ace for code input formatting
code = st_ace(language=language.lower(), theme='monokai', font_size=14, height=300, auto_update=True)

# Field for standard input
stdin = st.text_area("Standard Input", height=100)

if st.button("Run Code"):
    output = run_code(language, code, stdin)
    st.text_area("Output", output, height=300)
