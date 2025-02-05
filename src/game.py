"""
This module contains the `Game` class which represents a tennis game.
"""
from src.tennis_entity import TennisEntity


class Game(TennisEntity):
    """
    Represents a tennis game between two players.

    Attributes:
        winner (str): Winner of the game.
        current_point (int): Current point number.
        points (list): List of points in the game.
    """
    def __init__(self, player1: str, player2: str) -> None:
        """
        Initializes a new game with the given players.

        Args:
            player1 (str): Name of the first player.
            player2 (str): Name of the second player.
        """
        super().__init__(player1, player2)
        self.winner = None
        self.current_point = 1
        self.points = []
