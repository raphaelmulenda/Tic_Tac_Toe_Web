"""Created by Raphael Mulenda
date 27-04-2027
Tic Tac Toe Web Version"""

from flask import request, Flask, render_template, redirect

app = Flask(__name__)


class TicTacToeGame:
    def __init__(self):
        self.board = ["", "", "", "", "", "", "", "", ""]
        self.game_round = 0
        self.game_result = ""

    def reset_game(self):
        self.board = ["", "", "", "", "", "", "", "", ""]
        self.game_result = ""
        self.game_round = 0

    def check_win(self):
        """This function will check is teh current mark win the game"""
        # check horizontal
        if self.board[0] == self.board[1] == self.board[2]:
            return self.board[0]
        elif self.board[3] == self.board[4] == self.board[5]:
            return self.board[3]
        elif self.board[6] == self.board[7] == self.board[8]:
            return self.board[6]
        # check vertical
        elif self.board[0] == self.board[3] == self.board[6]:
            return self.board[0]
        elif self.board[1] == self.board[4] == self.board[7]:
            return self.board[1]
        elif self.board[2] == self.board[5] == self.board[8]:
            return self.board[2]
        # check diagonal
        elif self.board[0] == self.board[4] == self.board[8]:
            return self.board[0]
        elif self.board[2] == self.board[4] == self.board[6]:
            return self.board[2]
        # no winner
        return False

    def play_game(self, pressed_btn):
        if pressed_btn == "reset":
            self.reset_game()
            return self
        # Assign a Marker to players
        if self.game_round % 2 == 0:
            self.board[int(pressed_btn)] = "X"
        else:
            self.board[int(pressed_btn)] = "O"
        self.game_round += 1

        # check_win:
        game_winner = self.check_win()
        if game_winner:
            self.game_result = f"Player {game_winner} Won!"
            # if a user won the game we should disable the others buttons
            for x in range(9):
                if self.board[x] == "":
                    self.board[x] = " "
        elif not game_winner and self.game_round >= 9:
            self.game_result = "IT'S DRAW GAME🤝"

        # Reset_game


        return self


tic_tac_toe_game = TicTacToeGame()


@app.route('/', methods=["GET", "POST"])
@app.route('/tic_tac_toe', methods=['GET', 'POST'])
def play_game():
    if request.method == "POST":
        pressed_btn = request.form["clicked-btn"]
        tic_tac_toe_game.play_game(pressed_btn=pressed_btn)

    return render_template('index.html', board=tic_tac_toe_game.board, game_result=tic_tac_toe_game.game_result)


if __name__ == '__main__':
    app.run(debug=True)
