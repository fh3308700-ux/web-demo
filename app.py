import streamlit as st

# Page config
st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #1b973a, #4bd09b);
    }
    .title {
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        color: #ff6347;  /* Changed title color to a vibrant color */
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
    .button-cell {
        height: 150px !important;  /* Increased cell height */
        width: 150px !important;   /* Increased cell width */
        font-size: 48px !important;  /* Increased font size */
        border-radius: 12px !important;
        font-weight: bold !important;
        background-color: #483D8B;  /* Changed cell color to bright yellow */
        border: 3px solid  #4B0082;  /* Slightly darker yellow for the border */
        color: #003366;
        margin: 5px;
        transition: all 0.3s ease;
    }
    .button-cell:hover {
        background-color: #fbc02d;  /* Darker yellow when hovered */
        color: skyblue;
        transform: scale(1.1);  /* Zoom effect on hover */
    }
    .restart-button {
        font-size: 20px;
        padding: 10px 30px;
        border-radius: 10px;
        margin-top: 30px;
        background-color: #4CAF50;
        color: yellow;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Game title
st.markdown('<div class="title">🎮 Tic-Tac-Toe Game</div>', unsafe_allow_html=True)

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [["_" for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

def check_winner(board):
    for i in range(3):
        if board[i][0] != "_" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != "_" and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] != "_" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "_" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def is_draw(board):
    return all(cell != "_" for row in board for cell in row)

def reset_game():
    st.session_state.board = [["_" for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

# Game status
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif st.session_state.game_over:
    st.warning("It's a draw!")
else:
    st.markdown(f'<div class="turn-text">Player {st.session_state.current_player}\'s turn</div>', unsafe_allow_html=True)

# Game board
st.markdown('<div class="game-container">', unsafe_allow_html=True)
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell_value = st.session_state.board[i][j]
        cell_display = cell_value if cell_value != "_" else " "
        button_label = f"{cell_display}"

        if cols[j].button(button_label, key=f"{i}-{j}", help="Click to play", type="secondary"):
            if not st.session_state.game_over and st.session_state.board[i][j] == "_":
                st.session_state.board[i][j] = st.session_state.current_player
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                    st.session_state.game_over = True
                elif is_draw(st.session_state.board):
                    st.session_state.game_over = True
                else:
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
st.markdown('</div>', unsafe_allow_html=True)

# Restart button
st.markdown('<br>', unsafe_allow_html=True)
st.button("🔁 Restart Game", on_click=reset_game)

