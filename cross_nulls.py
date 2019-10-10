""""
contains class that implemets game CROSS&NULLS with AI
"""

import random

class GameCN:
    """
    this class present cross&nulls game with bot
    you start first
    before all your turn you see GameField

    | 0 | 0 | 0 |

    | 0 | 1 | 0 |

    | 0 | 0 | 2 |

    where 0 - is empty cell, 1 - your X and 2 id O
    Also it has protection from invalid inputs
    """
    field = [[0 for i in range(3)] for j in range(3)]
    curr_player = 1  # 1 - first(human), 2 - second(bot)
    winner = 0  # 0 - undefined, 1 - first, 2 - second, 3 - draw

    def put(self, _x, _y):
        """set figure of current player to field"""
        self.field[_x][_y] = self.curr_player
        self.check_end_of_game()
        self.curr_player = (self.curr_player) % 2 + 1

    def check_end_of_game(self):
        """check state of field on the end of game"""
        self.winner = 3
        for row in self.field:
            for _el in row:
                if _el == 0:
                    self.winner = 0

        for row in self.field:
            if row == [1, 1, 1]:
                self.winner = 1
            if row == [2, 2, 2]:
                self.winner = 2

        for n_col in range(3):
            col = [self.field[n_row][n_col] for n_row in range(3)]
            if col == [1, 1, 1]:
                self.winner = 1
            if col == [2, 2, 2]:
                self.winner = 2

        if([self.field[i][i] for i in range(3)] == [1, 1, 1] or
           [self.field[i][2 - i] for i in range(3)] == [1, 1, 1]):
            self.winner = 1

        if([self.field[i][i] for i in range(3)] == [2, 2, 2] or
           [self.field[i][2 - i] for i in range(3)] == [2, 2, 2]):
            self.winner = 2


    def strat_game(self):
        """
        start loop of game that ends when sb win
        or game was stopped
        """
        random.seed(20)
        self.draw_field()
        while self.winner == 0:
            self.human()
            self.bot()
            self.draw_field()

        if self.winner == 3:
            print("DRAW!")
        else:
            print(f"WINNER IS THE {self.winner} PLAYER!!!")

    def human(self):
        """
        handles user's turn
        """
        while True:
            flag, _x, _y = self.correct_input(
                input("\n Enter coordinate of point(from left, up corner): ")
                )
            if flag and self.field[_x][_y] == 0:
                self.put(_x, _y)
                return
            print("Incorrect input!")

    def bot(self):
        """realization of AI"""
        #checks self win
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == 0:
                    self.field[i][j] = 2
                    self.check_end_of_game()
                    if self.winner == 2:
                        self.put(i, j)
                        return
                    self.field[i][j] = 0
                    self.winner = 0

        #checks not lose
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == 0:
                    self.field[i][j] = 1
                    self.check_end_of_game()
                    if self.winner != 0:
                        self.put(i, j)
                        return
                    self.field[i][j] = 0
                    self.winner = 0

        for i in range(3):
            for j in range(3):
                if self.field[i][j] == 0:
                    self.put(i, j)
                    return

    def draw_field(self):
        """print in cli currant state of the field of game"""
        for row in self.field:
            print(f"\n| {row[0]} | {row[1]} | {row[2]} |")

    @staticmethod
    def correct_input(_input):
        """checks user's input on correctness"""
        try:
            _x, _y = map(int, _input.split())
        except ValueError:
            return (False, 0, 0)
        if isinstance(_y, int) and isinstance(_y, int) and _x in range(3) and _y in range(3):
            return (True, _x, _y)
        return (False, 0, 0)




if __name__ == "__main__":
    GAME = GameCN()
    GAME.strat_game()
