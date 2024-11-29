import streamlit as st
import math

# Set page config for better UI
st.set_page_config(page_title="RAAM's Calculator", page_icon="🧮", layout="centered")

# Custom CSS for modern styling
st.markdown("""
    <style>
    body {
        background-color: red !important;  # Added !important to enforce red background
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stTextInput, .stButton button {
        font-size: 1.2em;
        padding: 0.5em;
        border-radius: 8px;
    }
    .stButton button {
        background-color: #0078D7;
        color: white;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #005A9E;
    }
    .result-box {
        padding: 1em;
        border-radius: 8px;
        background-color: #fff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 1em;
        color: #333;  /* Ensures the text is dark and visible */
    }
    </style>
    """, unsafe_allow_html=True)

# App Title
st.title("PuPPus Calculator")

# Input Section
expression = st.text_input("Enter your mathematical expression:", "", help="Example: 2+2, 5*3, math.sin(math.pi/2)")

# Calculate and Display Result
if st.button("Calculate"):
    try:
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, {"math": math})
        st.markdown(f"<div class='result-box'><h2>Result: {result}</h2></div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error: {e}")

# Footer Section
st.markdown("""
    Built with ❤️ on PuPPu Ji
""")

