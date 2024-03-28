import streamlit as st
from html.parser import HTMLParser

class DivTagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            self.stack.append(self.getpos())

    def handle_endtag(self, tag):
        if tag == "div":
            if not self.stack:
                self.errors.append(f"Unopened div tag closed at {self.getpos()}")
            else:
                self.stack.pop()

    def check_html(self, html_content):
        self.feed(html_content)
        while self.stack:
            pos = self.stack.pop()
            self.errors.append(f"Unclosed div tag opened at {pos}")
        return self.errors

def check_html_divs(html_content):
    checker = DivTagChecker()
    errors = checker.check_html(html_content)
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
