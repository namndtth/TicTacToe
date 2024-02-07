import sys
from typing import *
from PySide6.QtCore import QSize
from PySide6.QtWidgets import *
from PySide6.QtGui import QFont

BUTTON_SIZE = QSize(100, 100)
BUTTON_KEY = '{}{}'


class View(QMainWindow):
    def __init__(self):
        self.buttons: Dict[str, QPushButton] = {}

        self.new_game_button = QPushButton('New Game')
        self.new_game_button.setFixedHeight(50)
        super().__init__()
        self.setWindowTitle('Tic Tac Toe')
        board = self.draw_board()
        board.addWidget(self.new_game_button, 3, 1, 1, 2)
        widget = QWidget(self)
        widget.setLayout(board)
        self.setCentralWidget(widget)

    def draw_board(self):
        board = QGridLayout()

        for i in range(3):
            for j in range(3):
                button = QPushButton('')
                button.setFixedSize(BUTTON_SIZE)
                button.setFont(QFont('', 32))
                board.addWidget(button, i, j)

                self.buttons[BUTTON_KEY.format(i, j)] = button

        return board

    def reset(self):
        for button in self.buttons.values():
            button.setDisabled(False)
            button.setText('')

    def disable_all(self):
        for button in self.buttons.values():
            button.setDisabled(True)

    def get_buttons(self):
        return self.buttons

    def set_button_text(self, row, col, symbol):
        button: QPushButton = self.buttons[BUTTON_KEY.format(row, col)]
        button.setText(symbol)

    def annount_winner(self, winner):
        print('Congrats ', winner, ' winner the game!')

    def annount_tie(self):
        print('Game is over with tie.')


if __name__ == '__main__':
    App = QApplication()
    window = View()
    window.show()
    sys.exit(App.exec())
