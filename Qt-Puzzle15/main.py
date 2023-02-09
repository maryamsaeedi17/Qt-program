import random
from functools import partial
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

def make_unrepeated_random_list():
    random_array=[]

    for i in range(16):
        random_num=random.randint(1,16)

        while random_num in random_array:
            random_num=random.randint(1,16)

        random_array.append(random_num)
    return random_array


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons=[[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
                      [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8],
                      [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
                      [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16]]

        my_list=make_unrepeated_random_list()
        k=0
        for i in range(4):
            for j in range(4):
                r=my_list[k]
                self.buttons[i][j].setText(str(r))
                k+=1
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
                if r==16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_row=i
                    self.empty_col=j

    def play(self, i, j):
        if abs(self.empty_row-i)+abs(self.empty_col-j)==1:
            self.buttons[self.empty_row][self.empty_col].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText("16")
            self.buttons[self.empty_row][self.empty_col].setVisible(True)
            self.buttons[i][j].setVisible(False)
            self.empty_row=i
            self.empty_col=j
        else:
            pass

        if self.check()==True:
            msg_box=QMessageBox(windowTitle="Congratulations", text="You win!🎉")
            msg_box.exec()

        

    
    def check(self):
        num=1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text())!=num:
                    return False
                num+=1
        return True

        
        




app=QApplication(sys.argv)

main_window=MainWindow()
main_window.show()

app.exec()