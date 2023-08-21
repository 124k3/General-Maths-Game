# Math Game Script

This is a simple Python script that generates a mathematical expression with random numbers and operators for the user to solve. The user is prompted to enter the correct result for the generated expression.

## Code Overview

The code defines a function `Game()` which generates a random mathematical expression and prompts the user to input the correct result. Here's an overview of the code structure and its functionality:

## Bages
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


### Generating the Expression

- A list called `OperstionsList` stores mathematical operators: `["+","-","*","+"]`. By editing the -1 index the game can be made more complex(changing "+" to "/")
- Lists `ProblemOperations` and `NumberList` are initialized for record-keeping purposes.
- A string `MathsProblem` is initialized to store the mathematical expression.
- Inside a loop, random numbers between 0 and 101 are generated and added to `MathsProblem`.
- For each number generated, a random operator is selected and added to `MathsProblem`.
- The `MathsProblem` string is converted to a list and manipulated to remove the last random operator.
- The modified `MathsProblem` is printed.

### Calculating and User Interaction

- The result of the expression is calculated using the `eval()` function.
- The user is prompted to input the final result.
- If the user's input matches the calculated result, they receive a success message and are prompted to restart the game.
- If the input is incorrect, the user receives a failure message and is prompted to restart the game.

### Restarting the Game

- The `EnterInput()` function handles user input and correctness checking.
- The `RestartGame()` function asks the user if they want to restart the game.
- If the user wants to restart, the `Game()` function is called again.

## How to Play

1. Run the script in a Python interpreter.
2. The script generates a random mathematical expression with numbers and operators.
3. Enter your calculated result for the expression.
4. The script will inform you whether your answer is correct or not.
5. You can choose to restart the game or exit.

## Note

- The code includes comments to provide explanations and improve code readability.

Have fun playing and solving mathematical expressions!
