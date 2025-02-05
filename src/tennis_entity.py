"""
This module contains the `TennisEntity` class
which represents common attributes for tennis entities.
"""

class TennisEntity:
    """
    Represents common attributes for tennis entities like players and scores.

    Attributes:
        player1 (str): Name of the first player.
        player2 (str): Name of the second player.
        score1 (int): Score of the first player.
        score2 (int): Score of the second player.
    """
    def __init__(self, player1: str, player2: str) -> None:
        """
        Initializes a new tennis entity with the given players.

        Args:
            player1 (str): Name of the first player.
            player2 (str): Name of the second player.
        """
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
