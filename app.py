import streamlit as st

# HTML and CSS code
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Tic-Tac-Toe Game</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background: white;
      margin: 0;
      padding: 0;
      width: 100vw;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      text-align: center;
    }

    h1 {
      color: #333;
      font-size: 40px;
      margin-bottom: 20px;
    }

    #turn {
      font-size: 28px;
      color: #444;
      margin-bottom: 20px;
    }

    .board {
      display: grid;
      grid-template-columns: repeat(3, 150px);
      grid-gap: 8px;
      background-color: #efefef;
      padding: 20px;
      border-radius: 15px;
      border: 5px solid black;
      position: relative;
    }

    .cell {
      width: 150px;
      height: 150px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 50px;
      font-weight: bold;
      color: white;
      background: #1c1515;
      border-radius: 10px;
      cursor: pointer;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      transition: background 0.3s ease, transform 0.3s ease;
    }

    .cell:hover {
      background-color: #777;
      transform: scale(1.05);
    }

    .cell.X {
      background: linear-gradient(45deg, #ff9800, #ff5722);
    }

    .cell.O {
      background: linear-gradient(45deg, #03a9f4, #0288d1);
    }

    .cell:active {
      transform: scale(0.95);
    }

    .winner-message {
      font-size: 30px;
      color: white;
      background-color: rgba(0, 0, 0, 0.8);
      padding: 30px;
      border-radius: 15px;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: none;
      text-align: center;
      width: 350px;
      height: 250px;
    }

    .close-btn {
      position: absolute;
      top: 5px;
      right: 10px;
      color: white;
      font-size: 25px;
      cursor: pointer;
    }

    #win-line {
      position: absolute;
      height: 5px;
      background: yellow;
      top: 0;
      left: 0;
      transform-origin: left center;
      transform: scaleX(0);
      transition: transform 0.5s ease;
      z-index: 10;
    }

    .play-again-btn {
      margin-top: 30px;
      font-size: 20px;
      padding: 10px 20px;
      border: none;
      border-radius: 8px;
      background-color: #28a745;
      color: white;
      cursor: pointer;
      transition: background 0.3s ease;
    }

    .play-again-btn:hover {
      background-color: #218838;
    }
  </style>
</head>
<body>

<h1>Tic-Tac-Toe Game</h1>
<p id="turn">Player X's turn</p>
<div id="board" class="board"></div>
<div id="win-line"></div>

<div id="winner-message" class="winner-message">
  <span id="close-btn" class="close-btn" onclick="closeWinnerMessage()">×</span>
  <div id="winner-text"></div>
  <button class="play-again-btn" onclick="resetGame()">Play Again</button>
</div>

<script>
let board = [
  ['_', '_', '_'],
  ['_', '_', '_'],
  ['_', '_', '_']
];
let currentPlayer = 'X';
let gameOver = false;
let resetTimeout = null;

function printBoard() {
  let boardHtml = '';
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      boardHtml += `<div class="cell" onclick="makeMove(${i}, ${j})">${board[i][j]}</div>`;
    }
  }
  document.getElementById('board').innerHTML = boardHtml;
}

function makeMove(row, col) {
  if (board[row][col] === '_' && !gameOver) {
    board[row][col] = currentPlayer;
    let cell = document.getElementsByClassName('cell')[row * 3 + col];
    cell.classList.add(currentPlayer);
    if (checkWinner()) {
      gameOver = true;
      setTimeout(() => {
        showWinner("Player " + currentPlayer + " wins!");
      }, 600);
    } else if (isBoardFull()) {
      gameOver = true;
      showWinner("It's a draw!");
    } else {
      currentPlayer = (currentPlayer === 'X') ? 'O' : 'X';
      document.getElementById('turn').innerText = "Player " + currentPlayer + "'s turn";
      printBoard();
    }
  }
}

function checkWinner() {
  for (let i = 0; i < 3; i++) {
    if (board[i][0] !== '_' && board[i][0] === board[i][1] && board[i][1] === board[i][2]) {
      drawWinLine(i, 0, i, 2);
      return true;
    }
    if (board[0][i] !== '_' && board[0][i] === board[1][i] && board[1][i] === board[2][i]) {
      drawWinLine(0, i, 2, i);
      return true;
    }
  }
  if (board[0][0] !== '_' && board[0][0] === board[1][1] && board[1][1] === board[2][2]) {
    drawWinLine(0, 0, 2, 2);
    return true;
  }
  if (board[0][2] !== '_' && board[0][2] === board[1][1] && board[1][1] === board[2][0]) {
    drawWinLine(0, 2, 2, 0);
    return true;
  }
  return false;
}

function drawWinLine(r1, c1, r2, c2) {
  const cellSize = 158;  // Approx cell size + padding
  const boardRect = document.getElementById('board').getBoundingClientRect();
  const x1 = c1 * cellSize + cellSize / 2;
  const y1 = r1 * cellSize + cellSize / 2;
  const x2 = c2 * cellSize + cellSize / 2;
  const y2 = r2 * cellSize + cellSize / 2;
  const dx = x2 - x1;
  const dy = y2 - y1;
  const length = Math.sqrt(dx * dx + dy * dy);
  const angle = Math.atan2(dy, dx) * 180 / Math.PI;
  const line = document.getElementById('win-line');
  line.style.top = `${y1 + boardRect.top}px`;
  line.style.left = `${x1 + boardRect.left}px`;
  line.style.width = `${length}px`;
  line.style.transform = `rotate(${angle}deg) scaleX(1)`;
}

function isBoardFull() {
  return board.flat().every(cell => cell !== '_');
}

function showWinner(message) {
  document.getElementById('winner-text').innerHTML = message;
  document.getElementById('winner-message').style.display = 'block';
  resetTimeout = setTimeout(() => {
    resetGame();
  }, 3000); // Auto-reset after 3 seconds
}

function closeWinnerMessage() {
  document.getElementById('winner-message').style.display = 'none';
  clearTimeout(resetTimeout);
}

function resetGame() {
  clearTimeout(resetTimeout);
  board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
  ];
  currentPlayer = 'X';
  gameOver = false;
  document.getElementById('turn').innerText = "Player X's turn";
  document.getElementById('winner-message').style.display = 'none';
  document.getElementById('win-line').style.transform = 'scaleX(0)';
  printBoard();
}

printBoard();
</script>

</body>
</html>
"""

# Show in Streamlit
st.set_page_config(layout="wide")
st.components.v1.html(html_code, height=1000, scrolling=False)
