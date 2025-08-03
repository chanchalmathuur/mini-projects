let currentPlayer = "X";
let gameActive = true;
let gameState = ["", "", "", "", "", "", "", "", ""];

const statusDisplay = document.getElementById("status");

const winningConditions = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
];

function handleCellClick(e) {
  const clickedCell = e.target;
  const clickedIndex = parseInt(clickedCell.dataset.index);

  if (gameState[clickedIndex] !== "" || !gameActive) return;

  gameState[clickedIndex] = currentPlayer;
  clickedCell.textContent = currentPlayer;

  checkResult();
}

function checkResult() {
  for (let condition of winningConditions) {
    const [a, b, c] = condition;
    if (
      gameState[a] &&
      gameState[a] === gameState[b] &&
      gameState[b] === gameState[c]
    ) {
      statusDisplay.textContent = `Player ${currentPlayer} wins!`;  // ✅ FIXED
      gameActive = false;
      return;
    }
  }

  if (!gameState.includes("")) {
    statusDisplay.textContent = "It's a draw!";
    gameActive = false;
    return;
  }

  currentPlayer = currentPlayer === "X" ? "O" : "X";
  statusDisplay.textContent = `Player ${currentPlayer}'s turn`; // ✅ FIXED
}

function resetGame() {
  currentPlayer = "X";
  gameActive = true;
  gameState = ["", "", "", "", "", "", "", "", ""];

  document.querySelectorAll(".cell").forEach((cell) => (cell.textContent = ""));
  statusDisplay.textContent = `Player ${currentPlayer}'s turn`; // ✅ FIXED
}

document.querySelectorAll(".cell").forEach((cell) =>
  cell.addEventListener("click", handleCellClick)
);
