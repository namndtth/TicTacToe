from functools import partial
from typing import *

from PySide6.QtWidgets import QPushButton

from view import View
from model import Model
from constants import *


class Controller:
    def __init__(self, model, view):
        self.model: Model = model
        self.view: View = view

        self.turn = TURN.X

        self.connect_buttons_callbacks()

    def connect_buttons_callbacks(self):
        buttons: Dict[str, QPushButton] = self.view.get_buttons()
        for key, button in buttons.items():
            button.clicked.connect(partial(self.on_cell_clicked, key))

        self.view.new_game_button.clicked.connect(self.on_new_game_clicked)

    def on_new_game_clicked(self):
        self.view.reset()
        self.model.reset()
        self.turn = TURN.X

    def on_cell_clicked(self, key: str):
        row, col = map(int, list(key))
        if self.model.cells[row][col]:
            return

        self.model.cells[row][col] = self.turn
        self.view.set_button_text(row, col, self.turn)

        winner = self.model.who_wins()
        if winner:
            self.view.annount_winner(winner)
            self.view.disable_all()
        elif self.model.nempty_cells() == 0:
            self.view.annount_tie()
            self.view.disable_all()

        if self.turn == TURN.X:
            self.turn = TURN.O
        else:
            self.turn = TURN.X

    def run(self):
        self.view.show()
