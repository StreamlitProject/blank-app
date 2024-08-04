import streamlit as st
from jdoodle import Jdoodle
from codemirror import CodeMirror

# Create a JDoodle instance
jdoodle = Jdoodle(api_key="YOUR_API_KEY")

# Create a CodeMirror instance
code_mirror = CodeMirror(
    value="# Write your code here",
    mode="python",
    theme="material",
    height=500,
    width=800
)

# Streamlit app
st.title("Interactive Coding Environment")

# Language selection
language = st.selectbox("Select a language", ["Python", "Java"])

# Code editor
st.write("Write your code below:")
code_editor = st.text_area("", value=code_mirror.value, height=500)

# Compile and run button
st.button("Compile and Run")

# Output area
st.write("Output:")
output_area = st.text_area("", height=200)

# Compile and run logic
if st.button("Compile and Run"):
    # Get the code from the editor
    code = code_editor.value

    # Set the language for JDoodle
    if language == "Python":
        language_id = 71  # Python 3
    elif language == "Java":
        language_id = 62  # Java 8

    # Compile and run the code using JDoodle
    result = jdoodle.compile_and_run(code, language_id)

    # Display the output
    output_area.value = result.output
