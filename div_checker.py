import streamlit as st

def find_div_issues(html_lines):
    stack = []  # To store line numbers of opened <div> tags
    issues = []  # To collect issues found

    for line_num, line in enumerate(html_lines, start=1):
        # Check for <div> opening tags
        if '<div>' in line:
            stack.append(line_num)
        # Check for <div> closing tags
        if '</div>' in line:
            if stack:
                stack.pop()  # Correctly closed <div>, remove from stack
            else:
                # Found closing tag without matching opening tag
                issues.append(f"Line {line_num}: Unmatched closing </div> tag.")
    
    # Any remaining opening <div> tags in stack are unmatched
    for line_num in stack:
        issues.append(f"Line {line_num}: Unmatched opening <div> tag.")

    return issues

st.title("HTML <div> Tag Checker")

# Upload HTML content
uploaded_file = st.file_uploader("Upload your HTML file", type="html")

if uploaded_file is not None:
    # Read and decode the file
    html_content = uploaded_file.getvalue().decode("utf-8").split('\n')
    
    # Find issues
    div_issues = find_div_issues(html_content)

    if div_issues:
        st.write("Issues found with <div> tags:")
        for issue in div_issues:
            st.write(issue)
    else:
        st.write("No issues found with <div> tags.")



# Add "Developed by Aditya" at the bottom of the Streamlit app interface
st.markdown("---")
st.markdown("Developed by Aditya")
