"""
This module contains the `Game` class which represents a tennis game.
"""
class Game:
    """
    Represents a tennis game between two players.

    Attributes:
        player1 (str): Name of the first player.
        player2 (str): Name of the second player.
        score1 (int): Score of the first player.
        score2 (int): Score of the second player.
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
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        self.winner = None
        self.current_point = 1
        self.points = []
