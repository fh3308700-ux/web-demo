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

    h1 {
      color: white;
      font-size: 40px;
      margin-bottom: 20px;
      text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }

    #turn {
      font-size: 40px;
      color: rgb(246, 241, 241);
      margin-bottom: 20px;
      text-shadow: 4px 4px 10px rgba(0,0,0,0.3);
    }

    .board {
      display: grid;
      grid-template-columns: repeat(3, 120px);
      grid-gap: 5px;
      justify-content: center;
      align-items: center;
      margin-top: 20px;
      background-color: #ef9c9c;
      padding: 20px;
      border-radius: 15px;
      border: 5px solid black;
      position: relative;
      width: 400px; /* Fixed width */
      height: 450px; /* Fixed height */
    }

    .cell {
      width: 120px;
      height: 120px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 40px;
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
      background: linear-gradient(45deg, hsl(36, 100%, 50%), #ff5722);
    }

    .cell.O {
      background: linear-gradient(45deg, #03a9f4, #0288d1);
    }

    .cell:active {
      transform: scale(0.95);
    }

    .winner-message {
      font-size: 40px;
      color: white;
      background-color: rgba(0, 0, 0, 0.8);
      padding: 40px;
      border-radius: 15px;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: none;
      text-align: center;
      width: 350px;
      height: 300px;
      z-index: 100;
    }

    .close-btn {
      position: absolute;
      top: 5px;
      right: 10px;
      color: rgb(242, 239, 245);
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
      font-size: 24px;
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
// Game logic remains unchanged
</script>

</body>
</html>
