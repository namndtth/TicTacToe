import sys

from PySide6.QtWidgets import QApplication

from view import View
from model import Model
from controller import Controller


def main():
    app = QApplication()
    view = View()
    model = Model()
    controller = Controller(model, view)
    controller.run()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
