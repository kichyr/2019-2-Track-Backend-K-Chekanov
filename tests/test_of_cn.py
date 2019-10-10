import sys
from io import StringIO
from cross_nulls import GameCN

def test_check_end_of_game():
    game = GameCN()
    game.field = [
        [1, 1, 1],
        [0, 2, 2],
        [0, 0, 0]
    ]
    game.check_end_of_game()
    assert game.winner == 1
    game.field = [
        [1, 2, 1],
        [0, 1, 2],
        [1, 0, 0]
    ]
    game.check_end_of_game()
    assert game.winner == 1

def test_put():
    game = GameCN()
    game.field = [
        [1, 1, 1],
        [0, 2, 2],
        [0, 0, 0]
    ]
    game.curr_player = 1
    game.put(1, 0)
    assert game.curr_player == 2 and game.field == [
        [1, 1, 1],
        [1, 2, 2],
        [0, 0, 0]
    ]

'''
def test_human():
    game = GameCN()
    sys.stdin = StringIO('asds dsdf')

    game.human()
    assert sys.stdout.read() == "Incorrect input!"
    sys.stdin = StringIO('1 1')
    game.human()
    assert sys.stdout.read() == ""
    assert game.curr_player == 2 and game.field == [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    sys.stdin = StringIO('1 1')
    game.human()
    assert sys.stdout.read() == "Incorrect input!"
'''
