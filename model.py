import numpy as np
from constants import *


class Model:
    def __init__(self):
        self.cells = np.array([[''] * 3 for _ in range(3)])

    def set_cell(self, row, col, symbol):
        if self.cells[row][col]:
            return
        self.cells[row][col] = symbol

    def is_winner(self, who):
        for row in self.cells:
            if np.all(row == who):
                return True

        for col in self.cells.T:
            if np.all(col == who):
                return True

        diag = self.cells.diagonal()
        if np.all(diag == who):
            return True

        anti_diag = np.fliplr(self.cells).diagonal()
        if np.all(anti_diag == who):
            return True

        return False

    def who_wins(self):

        if self.is_winner(XWIN):
            return XWIN

        if self.is_winner(OWIN):
            return OWIN

        return None

    def nempty_cells(self):
        return np.sum(self.cells == '')

    def reset(self):
        self.cells = np.array([[''] * 3 for _ in range(3)])
