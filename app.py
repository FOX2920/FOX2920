import streamlit as st
from markdown import markdown

def load_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        readme_text = f.read()
    return readme_text

def main():
    st.title("Streamlit Profile Website from README.md")
    readme_text = load_readme()
    st.markdown(markdown(readme_text), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
