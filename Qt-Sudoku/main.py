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
        self.ui.open_file_menu.triggered.connect(self.open_file)
        self.line_edits=[[None for i in range(9)] for j in range(9)]
        self.new_game()

    def open_file(self):
        file_path=QFileDialog.getOpenFileName(self, "Open file...")[0]
        f=open(file_path, "r")
        big_text=f.read()
        rows=big_text.split("\n")
        puzzle_board=[[None for i in range(9)] for j in range(9)]
        for i in range(len(rows)):
            cells=rows[i].split(" ")
            for j in range(len(cells)):
                puzzle_board[i][j]=int(cells[j])

        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setReadOnly(False)
                if puzzle_board[i][j] != 0:
                    self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")





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

    def check(self):
        for i in range(9):
            nums = []
            for j in range(9):
                num = self.line_edits[i][j].text()
                if num != "":
                    if num in nums:
                        return False
                    else:
                        nums.append(num)

        for i in range(9):
            nums = []
            for j in range(9):
                num = self.line_edits[j][i].text()
                if num != "":
                    if num in nums:
                        return False
                    else:
                        nums.append(num)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = []
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        num = self.line_edits[k][l].text()
                        if num != "":
                            if num in nums:
                                return False
                            else:
                                nums.append(num)




    def validation(self, i, j, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")

        if self.check() == False:
            self.line_edits[i][j].setStyleSheet("color: red; background-color: pink;")
        else:
            self.line_edits[i][j].setStyleSheet("color: blue; background-color: rgb(157, 195, 230);")
            for k in range(9):
                for l in range(9):
                    if self.line_edits[k][l] == "":
                        break
            else:
                msg_box = QMessageBox()
                msg_box.setText("You win!")



if __name__ == "__main__":
    app=QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

