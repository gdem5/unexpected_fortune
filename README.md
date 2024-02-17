# Password Guesser Game

Welcome to the Password Guesser Game, a fun and interactive command-line game that challenges players to guess the letters of a hidden password, reminiscent of the classic hangman game. Utilizing Python for logic and the Colorama library for an enhanced visual experience, this game is sure to provide hours of entertainment.

## Features

- **Interactive Gameplay:** Players are prompted to guess letters of a hidden word, making the gameplay intuitive and engaging.
- **Color-Coded Feedback:** Leveraging the Colorama library, the game provides immediate visual feedback by highlighting correct guesses in green, enhancing the user experience.
- **Customizable Word List:** The game dynamically loads words from a text file, allowing for easy customization of the game's difficulty and themes.

## Getting Started

### Prerequisites

Before you start, ensure you have the following installed:
- Python (3.6 or later recommended)
- Colorama package for Python

### Installation

1. **Clone the Repository**

    First, clone this repository to your local machine using Git:

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the Project Directory**

    Change into the project directory:

    ```bash
    cd <project-directory>
    ```

3. **Install Dependencies**

    Install the required Python package, Colorama:

    ```bash
    pip install colorama
    ```

## How to Play

1. **Prepare Your Word List**

    Create a text file named `fortune.txt` in the project directory. This file should contain words, each on a new line, which the game will use as potential passwords.

2. **Launch the Game**

    Run the game script with Python from your terminal:

    ```bash
    python <script-name>.py
    ```

3. **Gameplay**

    - The game will display a series of underscores representing the letters of the hidden word.
    - Input a letter when prompted. If the letter is in the word, it will be revealed in its correct positions.
    - The game continues until you guess all letters correctly or exhaust your attempts.

### Input/Output

- **Input:** The game prompts the player to input one letter at a time.
- **Output:** The game displays the current state of the guessed word, with correctly guessed letters revealed and the rest hidden as underscores. Correct guesses are highlighted in green.

## Acknowledgments

- Thanks to [Colorama](https://pypi.org/project/colorama/) for enabling colorful terminal output.
- A big shoutout to the Python community for continuous inspiration and support.

Happy guessing!
