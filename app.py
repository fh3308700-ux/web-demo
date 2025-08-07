import streamlit as st
from streamlit.components.v1 import html

# Streamlit page config
st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

# Wrap the entire HTML block in a raw triple-quoted string
game_html = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Tic-Tac-Toe Game</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background: linear-gradient(to right, #1b973a, #4bd09b);
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      flex-direction: column;
    }
    /* ... your CSS continues ... */
  </style>
</head>
<body>
  <!-- your HTML and JavaScript content -->
</body>
</html>
"""

# Streamlit content
st.title("Tic-Tac-Toe Game")
st.write("This is a simple Tic-Tac-Toe game implemented in HTML and JavaScript.")

# Display HTML content inside Streamlit
html(game_html, height=850)
