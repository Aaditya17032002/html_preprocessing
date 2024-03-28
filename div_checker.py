import streamlit as st

def check_html_divs(html_content):
    lines = html_content.split('\n')
    stack = []  # Stack to keep track of opening div tags (line number, line content)
    errors = []

    for i, line in enumerate(lines, start=1):
        if '<div' in line:  # Found opening div tag
            stack.append((i, line))
        if '</div>' in line:  # Found closing div tag
            if stack:
                stack.pop()  # Properly closed div, remove last opened div from stack
            else:
                errors.append(f"Line {i} has unopened closing div: {line.strip()}")
    
    # Any remaining opening divs in stack are unclosed
    for opening_line, content in stack:
        errors.append(f"Line {opening_line} has unclosed opening div: {content.strip()}")
    
    return errors

st.title("HTML Div Checker")

uploaded_file = st.file_uploader("Upload your HTML file", type="html")

if uploaded_file is not None:
    content = uploaded_file.getvalue().decode("utf-8")
    errors = check_html_divs(content)
    if errors:
        st.write("Errors found:")
        for error in errors:
            st.write(error)
    else:
        st.write("No missing opening or closing div tags found.")


# Add "Developed by Aditya" at the bottom of the Streamlit app interface
st.markdown("---")
st.markdown("Developed by Aditya")
