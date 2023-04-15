from player import RandomComputerPlayer, HumanPlayer
import time

class TicTakToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None#keeps track of current winner

    def print_board(self):
        # first get the rows
        for rows in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(rows) + ' | ')


    @staticmethod
    def print_board_number(): #print what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')


    def available_move(self):
        return [i for i, slot in enumerate(self.board) if slot == " "]

    def empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #we check if the square is empty and assign that position to th current letter
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #chek for row, column and diagonals
        row_ind = square//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([slot == letter for slot in row]):
            return True
#         check for column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([slot == letter for slot in row]):
            return True

#         check for diagonals
        if square % 2==0: #check if square is an even number
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([slot == letter for slot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([slot == letter for slot in diagonal1]):
                return True

        return False







def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_number()

    letter = 'x'#starting letter
    #kkep looping while the game still have empty space
    while game.empty_squares():
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)



        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} user makes a move to square {square}")
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(letter +" wins!")
                return letter
            letter = "o" if letter == "x" else "x"

        #wait for 2seconds before
        time.sleep(2)


    if print_game:
        print('it\'s a tie')

if __name__ == "__main__":
    x_player = HumanPlayer('x')
    y_player = RandomComputerPlayer('o')
    t = TicTakToe()
    play(t, x_player, y_player, print_game=True)