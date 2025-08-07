import streamlit as st

st.title("🎮 Tic-Tac-Toe Game")

if "board" not in st.session_state:
    st.session_state.board = [["_" for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

def check_winner(board):
    # Check rows, columns, diagonals
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

# Display turn
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif st.session_state.game_over:
    st.info("It's a draw!")
else:
    st.write(f"Player **{st.session_state.current_player}**'s turn")

# Display board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell = st.session_state.board[i][j]
        if cols[j].button(cell if cell != "_" else " ", key=f"{i}-{j}"):
            if cell == "_" and not st.session_state.game_over:
                st.session_state.board[i][j] = st.session_state.current_player
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                    st.session_state.game_over = True
                elif is_draw(st.session_state.board):
                    st.session_state.game_over = True
                else:
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

st.button("🔁 Restart Game", on_click=reset_game)
