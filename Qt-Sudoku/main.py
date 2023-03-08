import sys
import random
from functools import partial
from sudoku import Sudoku
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.new_menu.triggered.connect(self.new_game)
        self.line_edits=[[None for i in range(9)] for j in range(9)]
        self.new_game()
        
    def new_game(self):
        puzzle=Sudoku(3, seed=random.randint(1,1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                if puzzle.board[i][j] != None:
                    new_cell.setText(str(puzzle.board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell




    def validation(self, i, j, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")





if __name__ == "__main__":
    app=QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

