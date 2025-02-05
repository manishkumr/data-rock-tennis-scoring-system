"""
This module contains unit tests for the `Match` class.
"""

import unittest

from src.match import Match


class TestMatch(unittest.TestCase):

    """
    Test cases for the `Match` class.
    """
    def setUp(self):
        self.match = Match("player1", "player2")

    def test_initial_score(self):
        self.assertEqual(self.match.score(), "0-0, 0-0")

    def test_point_won_by_player1(self):
        self.match.point_won_by("player1")
        self.assertEqual(self.match.score(), "0-0, 15-0")

    def test_point_won_by_player2(self):
        self.match.point_won_by("player2")
        self.assertEqual(self.match.score(), "0-0, 0-15")

    def test_deuce(self):
        self.match.point_won_by("player1")
        self.match.point_won_by("player1")
        self.match.point_won_by("player1")
        self.match.point_won_by("player2")
        self.match.point_won_by("player2")
        self.match.point_won_by("player2")
        self.assertEqual(self.match.score(), "0-0, Deuce")

    def test_advantage_player1(self):
        self.match.point_won_by("player1")
        self.match.point_won_by("player1")
        self.match.point_won_by("player1")
        self.match.point_won_by("player2")
        self.match.point_won_by("player2")
        self.match.point_won_by("player2")
        self.match.point_won_by("player1")
        self.assertEqual(self.match.score(), "0-0, Advantage player1")

    def test_advantage_player2(self):
        self.match.point_won_by("player1")
        self.match.point_won_by("player1")
        self.match.point_won_by("player1")
        self.match.point_won_by("player2")
        self.match.point_won_by("player2")
        self.match.point_won_by("player2")
        self.match.point_won_by("player2")
        self.assertEqual(self.match.score(), "0-0, Advantage player2")

    def test_player1_wins_game(self):
        self.match.point_won_by("player1")
        self.match.point_won_by("player1")
        self.match.point_won_by("player1")
        self.match.point_won_by("player1")
        self.assertEqual(self.match.score(), "1-0")

    def test_player2_wins_game(self):
        self.match.point_won_by("player2")
        self.match.point_won_by("player2")
        self.match.point_won_by("player2")
        self.match.point_won_by("player2")
        self.assertEqual(self.match.score(), "0-1")

if __name__ == '__main__':
    unittest.main()
