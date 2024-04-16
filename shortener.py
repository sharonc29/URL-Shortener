import pyshorteners
import streamlit as st

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

#creamos app web con stremamlit
st.set_page_config(page_title="URL Shortener", page_icon="✏️", layout="centered")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgMBIhLAp2zFK83VMwx1XADC-oo0KeRZsn7w&s", use_column_width=True)
st.title(':blue[URL Shortener]')
url = st.text_input("Enter the URL")
if st.button("Generate new URL"):
    st.write("URL shortened: ", shorten_url(url))
    