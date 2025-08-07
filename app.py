st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #28a745, #4bd09b);
    }
    .title {
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        color: #ff6347;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    .turn-text {
        text-align: center;
        font-size: 1.5em;
        color: #fff;
        margin-bottom: 20px;
    }
    .game-container {
        background-color: #ef9c9c;
        border-radius: 20px;
        padding: 30px;
        width: 420px;
        margin: auto;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }
    button[kind="secondary"] {
        height: 100px !important;
        width: 100px !important;
        font-size: 36px !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        background-color: #1c1515 !important;
        border: 3px solid #ff9966 !important;
        color: #ffeb3b !important;
        margin: 5px !important;
        transition: all 0.3s ease !important;
    }
    button[kind="secondary"]:hover {
        background-color: #ff9966 !important;
        color: white !important;
        transform: scale(1.1) !important;
    }
    .restart-button {
        font-size: 20px;
        padding: 10px 30px;
        border-radius: 10px;
        margin-top: 30px;
        background-color: #28a745;
        color: white;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)
