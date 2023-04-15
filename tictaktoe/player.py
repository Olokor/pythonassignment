import random
import math

class Player:
    def __init__(self, letter):
        self.letter = letter

    #all player can  get their next move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_move())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        val_square = False
        val = None

        while not val_square:
            square = input(self.letter + '\'s turn input (o-8)')
            # check if the user enters a valued type and an empty space on the board
            try:
                val = int(square)
                if val not in game.available_move():
                    raise ValueError
                val_square = True #meaning the input is valued
            except ValueError:
                print("invalid square, try again")
        return val


class GeniusComputer(Player):
    def __init__(self, letter):
        super.__init__(letter)

    def get_move(self, game):
        if len(game.available_move()) == 9:
            square = random.choice(game.available_move())
        else:
            square = self.minimax(game, self.letter)
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'o' if player == 'x' else 'x'
