import streamlit as st
from prompt_builder import build_prompt
from categorizer import categorize_items

st.set_page_config(page_title="Grocery Categorizer", layout="centered")

st.title("Grocery List Categorizer (LLM Powered)")

items = st.text_area("Paste your grocery list (one item per line):", height=200)
language = st.selectbox("Language", ["English", "French", "Arabic"])
style = st.selectbox("Style", ["plain", "markdown", "bullet-points"])
tips = st.checkbox("Include shopping tips?")

if st.button("Categorize"):
    if items.strip() == "":
        st.warning("Please enter some grocery items.")
    else:
        prompt = build_prompt(items, language, style, tips)
        with st.spinner("Asking the LLM..."):
            result = categorize_items(prompt)
        st.subheader("Categorized Grocery List")
        st.code(result)
