import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

x_score=0
o_score=0
ties_num=0

def next_turn():
    global player
    for i in range(3):
        for j in range(3):
            button_array[i][j].setText("")
    player=1
    game_window.btn_turn.setText("X-turn")
    game_window.btn_turn.setStyleSheet("color: red;")

def new_game():
    global x_score
    global o_score
    global ties_num
    next_turn()
    game_window.btn_scr_x.setText("X score:" + "\n" + "0")
    game_window.btn_scr_o.setText("O score:" + "\n" + "0")
    game_window.btn_ties.setText("Ties:" + "\n" + "0")
    x_score=o_score=ties_num=0



def check():
    global x_score
    global o_score
    global  ties_num
    if (button_array[0][0].text()=="X" and button_array[0][1].text()=="X" and button_array[0][2].text()=="X") or (button_array[1][0].text()=="X" and button_array[1][1].text()=="X" and button_array[1][2].text()=="X") or (button_array[2][0].text()=="X" and button_array[2][1].text()=="X" and button_array[2][2].text()=="X") or (button_array[0][0].text()=="X" and button_array[1][0].text()=="X" and button_array[2][0].text()=="X") or (button_array[0][1].text()=="X" and button_array[1][1].text()=="X" and button_array[2][1].text()=="X") or (button_array[0][2].text()=="X" and button_array[1][2].text()=="X" and button_array[2][2].text()=="X") or (button_array[0][0].text()=="X" and button_array[1][1].text()=="X" and button_array[2][2].text()=="X") or (button_array[0][2].text()=="X" and button_array[1][1].text()=="X" and button_array[2][0].text()=="X"):
        x_score+=1
        game_window.btn_scr_x.setText("X score:" + "\n" + str(x_score))
        msg_box=QMessageBox(windowTitle="Result", text="player 1 won.")
        msg_box.exec()
        next_turn()
        
    elif (button_array[0][0].text()=="O" and button_array[0][1].text()=="O" and button_array[0][2].text()=="O") or (button_array[1][0].text()=="O" and button_array[1][1].text()=="O" and button_array[1][2].text()=="O") or (button_array[2][0].text()=="O" and button_array[2][1].text()=="O" and button_array[2][2].text()=="O") or (button_array[0][0].text()=="O" and button_array[1][0].text()=="O" and button_array[2][0].text()=="O") or (button_array[0][1].text()=="O" and button_array[1][1].text()=="O" and button_array[2][1].text()=="O") or (button_array[0][2].text()=="O" and button_array[1][2].text()=="O" and button_array[2][2].text()=="O") or (button_array[0][0].text()=="O" and button_array[1][1].text()=="O" and button_array[2][2].text()=="O") or (button_array[0][2].text()=="O" and button_array[1][1].text()=="O" and button_array[2][0].text()=="O"):
        o_score+=1
        game_window.btn_scr_o.setText("O score:" + "\n" + str(o_score))
        if game_mode=="p_vs_p":
            msg_box=QMessageBox(windowTitle="Result", text="player 2 won.")
            msg_box.exec()
            next_turn()
        elif game_mode=="p_vs_c":
            msg_box=QMessageBox(windowTitle="Result", text="CPU won.")
            msg_box.exec()
            next_turn()
    elif button_array[0][0].text()!="" and button_array[0][1].text()!="" and button_array[0][2].text()!="" and button_array[1][0].text()!="" and button_array[1][1].text()!="" and button_array[1][2].text()!="" and button_array[2][0].text()!="" and button_array[2][1].text()!="" and button_array[2][2].text()!="":
        ties_num+=1
        game_window.btn_ties.setText("Ties:" + "\n" + str(ties_num))
        msg_box=QMessageBox(windowTitle="Result", text="Tie!")
        msg_box.exec()
        next_turn()


def about():
    msg_box=QMessageBox(windowTitle="About game", text="Tic-tac-toe is a game in which two players take turns in drawing either an 'O' or an 'X' in one square of a grid consisting of nine squares. The winner is the first player to get three of the same symbols in a row or coloumn or diameter.")
    msg_box.exec()


def set_mode(m):
    global game_mode
    game_mode=m
    print(game_mode)
    new_game()

def play(row,col):
    global player
    global game_mode
    k=0

    if button_array[row][col].text()=="":
        if player==1:
            button_array[row][col].setText("X")
            button_array[row][col].setStyleSheet("color: red;")
            k+=1
            if game_mode=="p_vs_c":
                if k<9:
                    while True:
                        r=random.randint(0, 2)
                        c=random.randint(0, 2)
                        if button_array[r][c].text()=="":
                            button_array[r][c].setText("O")
                            button_array[r][c].setStyleSheet("color: blue")
                            k+=1
                            player=1
                            game_window.btn_turn.setText("X-turn")
                            game_window.btn_turn.setStyleSheet("color: red;")
                            break
            else:                
                player=2
                game_window.btn_turn.setText("O-turn")
                game_window.btn_turn.setStyleSheet("color: blue;")
        elif player==2:
            if game_mode=="p_vs_p":
                button_array[row][col].setText("O")
                button_array[row][col].setStyleSheet("color: blue;")
                k+=1
                player=1
                game_window.btn_turn.setText("X-turn")
                game_window.btn_turn.setStyleSheet("color: red;")

    check()


t_game=QApplication([])

player=1
game_mode="p_vs_p"
turn="X-turn"


loader=QUiLoader()
game_window=loader.load("Qt-TicTocToe/tictoctoe.ui")
game_window.show()

button_array=[[game_window.btn_1, game_window.btn_2, game_window.btn_3],
              [game_window.btn_4, game_window.btn_5, game_window.btn_6],
              [game_window.btn_7, game_window.btn_8, game_window.btn_9]]


for i in range(3):
    for j in range(3):
        button_array[i][j].clicked.connect(partial(play, i, j))


game_window.btn_newgame.clicked.connect(new_game)
game_window.btn_about.clicked.connect(about)


game_window.rdo_pp.pressed.connect(partial(set_mode, "p_vs_p"))
game_window.rdo_pc.pressed.connect(partial(set_mode, "p_vs_c"))


t_game.exec()
