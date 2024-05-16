import streamlit as st

def replace_text(input_text, old_substring, new_substring):
    return input_text.replace(old_substring, new_substring)

st.title("Text Replacement Application")

# User input for the text
input_text = st.text_area("Enter the text to be modified:")

# User input for the substring to replace and the new substring
old_substring = st.text_input("Enter the substring to be replaced:", value="plmgroup")
new_substring = st.text_input("Enter the new substring:", value="addinor")

# Button to perform the replacement
if st.button("Replace"):
    if input_text:
        modified_text = replace_text(input_text, old_substring, new_substring)
        st.text_area("Modified Text:", value=modified_text, height=200)
    else:
        st.warning("Please enter the text to be modified.")
