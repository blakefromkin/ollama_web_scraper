import streamlit as st
from scrape import scrape_website

st.title("AI Web Scraper")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    if url:
        st.write("Scraping the website...")
        result = scrape_website(url)
        print(result)
    else:
        st.write("Must enter valid URL.")
