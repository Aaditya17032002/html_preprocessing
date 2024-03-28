import streamlit as st
from html.parser import HTMLParser

class HTMLBeautifier(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.indent_level = 0
        self.beautified_html = ""

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            self.beautified_html += "    " * self.indent_level + f"<{tag}"
            for attr in attrs:
                self.beautified_html += f' {attr[0]}="{attr[1]}"'
            self.beautified_html += ">\n"
            self.indent_level += 1
        else:
            # Handle other tags if necessary
            pass

    def handle_endtag(self, tag):
        if tag == "div":
            self.indent_level -= 1
            self.beautified_html += "    " * self.indent_level + f"</{tag}>\n"
        else:
            # Handle other tags if necessary
            pass

    def handle_data(self, data):
        if data.strip():
            self.beautified_html += "    " * self.indent_level + data.strip() + "\n"

    def beautify_html(self, html_content):
        self.feed(html_content)
        return self.beautified_html

def beautify_html_content(html_content):
    beautifier = HTMLBeautifier()
    return beautifier.beautify_html(html_content)

st.title("HTML Beautifier with Div Structure Awareness")

uploaded_file = st.file_uploader("Upload your HTML file", type="html")

if uploaded_file is not None:
    content = uploaded_file.getvalue().decode("utf-8")
    beautified_html = beautify_html_content(content)
    
    st.text_area("Beautified HTML", beautified_html, height=300)




# Add "Developed by Aditya" at the bottom of the Streamlit app interface
st.markdown("---")
st.markdown("Developed by Aditya")
