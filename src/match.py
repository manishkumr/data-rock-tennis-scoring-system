"""
This module contains the `Match` class which represents a tennis match.
"""

from src.game import Game
from src.score_map import score_map
from src.tennis_entity import TennisEntity


class Match(TennisEntity):
    """
    Represents a tennis match between two players.

    Attributes:
        winner (str): Winner of the match.
        current_set (int): Current set number.
        sets (list): List of sets in the match.
        current_game (Game): Current game being played.
        games (list): List of games in the match.
    """
    def __init__(self, player1: str, player2: str) -> None:
        """
        Initializes a new match with the given players.

        Args:
            player1 (str): Name of the first player.
            player2 (str): Name of the second player.
        """
        super().__init__(player1, player2)
        self.winner = None
        self.current_set = 1
        self.sets = []
        self.current_game = Game(player1, player2)
        self.games = []

    def point_won_by(self, player: str) -> None:
        """
        Records a point won by the specified player.

        Args:
            player (str): Name of the player who won the point.
        """
        self.current_game.points.append(player)
        if player == self.player1:
            self.current_game.score1 += 1
        else:
            self.current_game.score2 += 1

        if (self.current_game.score1 >= 4 and
                self.current_game.score1 - self.current_game.score2 >= 2):
            # Player1 wins the game
            self.current_game.winner = self.player1
            self.score1 += 1
            # self.current_game = Game(self.player1, self.player2)
            # self.games.append(self.current_game)
        elif (self.current_game.score2 >= 4 and
              self.current_game.score2 - self.current_game.score1 >= 2):
            # Player2 wins the game
            self.current_game.winner = self.player2
            self.score2 += 1

    def score(self) -> str:
        """
        Returns the current score of the match.

        Returns:
            str: The current score of the match.
        """

        if self.current_game.winner is not None:
            return f"{self.score1}-{self.score2}"
        if self.current_game.score1 == 3 and self.current_game.score2 == 3:
            # Deuce
            return f"{self.score1}-{self.score2}, Deuce"
        if self.current_game.score1 == 4 and self.current_game.score2 == 3:
            # Advantage player1
            return f"{self.score1}-{self.score2}, Advantage {self.player1}"
        if self.current_game.score1 == 3 and self.current_game.score2 == 4:
            # Advantage player2
            return f"{self.score1}-{self.score2}, Advantage {self.player2}"

        return (f"{self.score1}-{self.score2}, "
                f"{score_map.get(self.current_game.score1)}-"
                f"{score_map.get(self.current_game.score2)}")
