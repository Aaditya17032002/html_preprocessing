import streamlit as st
from bs4 import BeautifulSoup

def process_html(input_html):
    # Parse the HTML
    soup = BeautifulSoup(input_html, 'html.parser')
    
    # Iterate over all <a> tags
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        # Conditions for modifying href attributes
        if href != "index.html" and "https://www.barodaweb.com/" not in href:
            a_tag['href'] = "#"
    
    # Add "Developed by Aditya" at the end of the document
    soup.body.append(soup.new_tag("p", string="Developed by Aditya"))
    
    # Return the modified HTML as a string
    return str(soup)

st.title('HTML File Processor')

# File uploader allows user to add their own HTML
uploaded_file = st.file_uploader("Choose a HTML file", type="html")

if uploaded_file is not None:
    # Read the content of the file
    content = uploaded_file.getvalue().decode("utf-8")
    
    # Process the HTML content
    processed_html = process_html(content)
    
    # Display processed HTML or allow download
    st.download_button(label="Download Processed HTML", data=processed_html, file_name="processed.html", mime="text/html")
