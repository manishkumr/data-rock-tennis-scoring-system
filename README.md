# Tennis Match Scoring System

## Overview

This project is a Python-based tennis match scoring system. It simulates a tennis match between two players, keeping track of the scores and determining the winner of each game and the match.

## Project Structure

```
data-rock-tennis-scoring-system/
|── src/
|   └──  game.py
|   └──  match.py
|   └──  score_map.py
├──  tests/
|   └── test_match.py
├── README.md
├── main.py
```

- **`main.py`**: Entry point of the application. It initializes a `Match` object and simulates a series of points won by players.
- **`match.py`**: Contains the `Match` class which represents a tennis match.
- **`game.py`**: Contains the `Game` class which represents a tennis game.
- **`score_map.py`**: Contains the `score_map` dictionary which maps integer scores to their corresponding string representations in a tennis game.
- **`test_match.py`**: Contains unit tests for the `Match` class.
- **`__init__.py`**: Initializes the package.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/manishkumr/data-rock-tennis-scoring-system.git

    cd data-rock-tennis-scoring-system/
    ```


## Usage

Run the `main.py` file to simulate a tennis match:

```sh
python main.py
```

## Running Tests

To run the unit tests, execute the following command:

```sh
python -m unittest tests.test_match
```

## Modules

### `main.py`

This module initializes a `Match` object and simulates a series of points won by players. It prints the current score after each point.

### `match.py`

This module contains the `Match` class which represents a tennis match between two players. It keeps track of the scores and determines the winner of each game and the match.

### `game.py`

This module contains the `Game` class which represents a tennis game between two players. It keeps track of the scores and determines the winner of the game.

### `score_map.py`

This module contains the `score_map` dictionary which maps integer scores to their corresponding string representations in a tennis game.

### `test_match.py`

This module contains unit tests for the `Match` class. It tests various scenarios such as initial score, points won by players, deuce, advantage, and game-winning conditions.

