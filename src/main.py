
from match import Match

if __name__ == '__main__':
    match = Match("player1", "player2")
    match.point_won_by("player1")
    match.point_won_by("player2")
    print(match.score())

    match.point_won_by("player1")
    match.point_won_by("player1")
    print(match.score())

    match.point_won_by("player2")
    match.point_won_by("player2")
    print(match.score())

    match.point_won_by("player1")
    print(match.score())

    match.point_won_by("player1")
    print(match.score())


