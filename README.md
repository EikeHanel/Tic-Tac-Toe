# Tic-Tac-Toe Game

Welcome to the Tic-Tac-Toe game! This is a simple two-player game implemented in Python. Players take turns marking a 3x3 grid, with the goal of getting three of their marks in a row, column, or diagonal.

## Features

- Two players can play the game interactively.
- Players take turns to place their marks (`o` and `x`) on the grid.
- The game checks for a win condition or a tie after each move.
- Option to play again after the game ends.

## Game Rules

- Player 1 uses the mark `o`.
- Player 2 uses the mark `x`.
- Players choose a spot on the grid using coordinates (e.g., `b2` for the center).
- The game will display the board after each move.
- The game announces the winner or a tie.
- Players are prompted to start a new game after a game ends.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Running the Game

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/EikeHanel/Tic-Tac-Toe.git
   cd Tic-Tac-Toe
2. **Run the Program:**
    ```
   python tictactoe.py

3. **Follow the Promts:**
- Enter the coordinates for your move when prompted.
- The board will be updated after each move.
- The game will notify you if there's a winner or if the game ends in a tie.
- You will be asked if you want to play again once a game ends.


### Code Overview
- `MARK_SPOT`: A dictionary representing the Tic-Tac-Toe board with initial empty spots ("-").
- `tictactoe_board(spot)`: Function to generate and return the current board state as a formatted string.
- `winner(spot)`: Function to check the current board state for a win condition or a tie.
- The main game loop handles player turns, board updates, and game state checks.
### Future Improvements
- Implement input validation to handle invalid or out-of-range coordinates.
- Add an option for single-player mode with AI.
- Improve the user interface with color or graphical representation.
### Contributing
Feel free to open issues or submit pull requests if you have suggestions for improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
