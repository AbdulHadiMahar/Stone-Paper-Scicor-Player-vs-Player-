# 🪨 Stone Paper Scissor — Player vs Player

A simple command-line Stone Paper Scissor game built with Python. Two players compete against each other in a 7-round match, enter their choices secretly, and earn points based on the game rules.

## 🎮 Features

- 👥 **Two-Player Mode:** Play against another person on the same computer.
- 🔒 **Hidden Choices:** Uses Python's `getpass` module to hide players' inputs.
- 🏆 **Score Tracking:** Keeps track of each player's points throughout the match.
- 🔄 **Seven Rounds:** Play a match consisting of 7 rounds.
- ✅ **Input Validation:** Checks whether players enter valid choices.
- 📊 **Live Scoreboard:** Displays the current score after each round.

## 🛠️ Technologies Used

- **Python 3**
- `getpass` module
- `while` loops
- `if-elif-else` conditional statements
- Lists and variables

## 📋 Game Rules

The game has three possible choices:

- 🪨 **Stone** beats Scissor.
- 📄 **Paper** beats Stone.
- ✂️ **Scissor** beats Paper.

If both players choose the same option, the round is a tie, and neither player earns a point.

Each winning round earns the winner one point.

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/stone-paper-scissor.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 3. Open the Project Folder

```bash
cd stone-paper-scissor
```

### 4. Run the Game

If your Python file is named `main.py`, run:

```bash
python main.py
```

On some systems, you may need to use:

```bash
python3 main.py
```

## 🎯 How to Play

1. Start the Python program.
2. Player 1 enters `stone`, `paper`, or `scicor`.
3. Player 2 enters their choice.
4. The program determines the round winner.
5. Check the updated score.
6. Continue until all 7 rounds have finished.

**Note:** The choices are entered without displaying them on the screen because the program uses `getpass`.

## 📂 Project Structure

```text
stone-paper-scissor/
├── main.py
└── README.md
```

## 📚 Learning Objectives

This project is useful for beginners learning Python programming. It demonstrates:

- Working with variables and data types.
- Taking user input.
- Using loops for repeated gameplay.
- Applying conditional logic to determine winners.
- Validating user input.
- Tracking scores with variables.
- Using Python's built-in `getpass` module.

## 🔮 Future Improvements

- Fix round numbering so it increments correctly.
- Display the final match result after all 7 rounds.
- Improve input validation and error handling.
- Handle tied rounds consistently.
- Add a graphical user interface.
- Add a Player vs Computer mode.

## 👨‍💻 Author

Created as a beginner Python programming project to practice loops, conditional statements, user input, and basic game logic.

## 📄 License

This project is open source. You may use, modify, and learn from the code.
