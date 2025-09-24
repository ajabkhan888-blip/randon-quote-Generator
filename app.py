import streamlit as st
import random

# List of quotes
QUOTES = [
    "The best way to predict the future is to create it.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Happiness is not something ready made. It comes from your own actions.",
    "Believe you can and you're halfway there.",
    "In the middle of every difficulty lies opportunity."
]

def get_random_quote():
    return random.choice(QUOTES)

# Streamlit app layout
st.set_page_config(page_title="Random Quote Generator", page_icon="✨", layout="centered")

st.title("✨ Random Quote Generator ✨")
st.write("Click the button below to get inspired!")

if st.button("Generate Quote"):
    quote = get_random_quote()
    st.success(quote)
