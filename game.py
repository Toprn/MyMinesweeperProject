from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys,random,time
from datetime import datetime
class Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 360)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.pressed(self.lineEdit.text(),self.lineEdit_2.text()))
        self.pushButton.setGeometry(QtCore.QRect(180, 220, 151, 71))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 130, 40))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 110, 130, 40))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 131, 61))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pressed(self,height,width):
        try:
            if int(height) not in range(10,51) or int(width) not in range(10,51):
                self.label_3.setText("Please enter\nnumber 10-50")
            elif int(height) in range(10,51) and int(width) in range(10,51):
                self.height = int(height)
                self.width = int(width)
                thisMainWindow.hide()
                GameWindow.show()
        except:
            self.label_3.setText("Alphabets\naren't allow")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Play now"))
        self.label.setText(_translate("MainWindow", "Height"))
        self.label_2.setText(_translate("MainWindow", "Width"))
        self.label_3.setText(_translate("MainWindow", ""))

class MainWindow(object):
    def __init__(self):
        self.height = Main.height
        self.width = Main.width
        self.label = []
        self.button = []
        self.mainheight = 25 * self.height + 40
        self.mainwidth = 25 * self.width + 150
        self.checkbomb = []
        for i in range(self.height):
            self.checkbomb.append([])
            for _ in range(self.width):
                chance = random.randint(0, 100)
                if chance < 15:
                    self.checkbomb[i].append("bomb")
                else:
                    self.checkbomb[i].append(".")
        for i in range(self.height):
            for j in range(self.width):
                if self.checkbomb[i][j] != "bomb":
                    bombs = 0
                    if i-1 >= 0:
                        if j-1 >= 0 and self.checkbomb[i-1][j-1] == "bomb":
                            bombs += 1
                        if self.checkbomb[i-1][j] == "bomb":
                            bombs += 1
                        if j+1 < self.width and self.checkbomb[i-1][j+1] == "bomb":
                            bombs += 1
                    if j-1 >= 0 and self.checkbomb[i][j-1] == "bomb":
                        bombs += 1
                    if j+1 < self.width and self.checkbomb[i][j+1] == "bomb":
                        bombs += 1
                    if i+1 < self.width:
                        if j-1 >= 0 and self.checkbomb[i+1][j-1] == "bomb":
                            bombs += 1
                        if self.checkbomb[i+1][j] == "bomb":
                            bombs += 1
                        if j+1 < self.width and self.checkbomb[i+1][j+1] == "bomb":
                            bombs += 1
                    self.checkbomb[i][j] = bombs

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.mainheight, self.mainwidth)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        for i in range(self.height):
            self.label.append([])
            self.button.append([])
        y=100
        z=0
        for i in range(self.height):
            x=20
            for j in range(self.width):
                self.label[i].append(QtWidgets.QLabel(self.centralwidget))
                self.label[i][j].setGeometry(QtCore.QRect(x, y, 25, 25))
                self.label[i][j].setText("")
                self.label[i][j].setPixmap(QtGui.QPixmap("empty-box.png"))
                self.label[i][j].setScaledContents(True)
                self.label[i][j].setObjectName("label"+str(i)+"_"+str(j))
                self.checkbombs(i,j)
                self.button[i].append(QtWidgets.QPushButton(self.centralwidget))
                self.button[i][j].setGeometry(QtCore.QRect(x, y, 25, 25))
                self.button[i][j].setText("")
                self.button[i][j].setIcon(QIcon('empty-box.png'))
                self.button[i][j].setObjectName("button"+str(i)+"_"+str(j))
                self.button[i][j].clicked.connect(lambda checked, arg1 = i, arg2=j: self.pressed(arg1,arg2))
                x += 25
                z+=1
            y += 25
        self.Timertext = QtWidgets.QLabel(self.centralwidget)
        self.Timertext.setGeometry(QtCore.QRect(30, 25, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Timertext.setFont(font)
        self.Timertext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Timertext.setAlignment(QtCore.Qt.AlignLeft)
        self.Timertext.setObjectName("Timer")
        self.count = 0
        self.flag = True
        self.Timer = QTimer(self.centralwidget)
        self.Timer.timeout.connect(self.showTime)
        self.Timer.start(100)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.sec = time.time()-time.time()
        self.mins = self.sec // 60
        self.sec = self.sec % 60
        self.hours = self.mins // 60
        self.mins = self.mins % 60
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.exit())
        self.ExitButton.setGeometry(QtCore.QRect(25*self.width - 50, 20, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ExitButton.setFont(font)
        self.ExitButton.setObjectName("ExitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showTime(self):
        if self.flag == True:
            self.count+= 1
            timenow = self.count / 10
            self.Timertext.setText(str(timenow))

    def checkbombs(self,i,j):
        if self.checkbomb[i][j] == 1:
            self.label[i][j].setPixmap(QtGui.QPixmap("1-box.png"))
        elif self.checkbomb[i][j] == 2:
            self.label[i][j].setPixmap(QtGui.QPixmap("2-box.png"))
        elif self.checkbomb[i][j] == 3:
            self.label[i][j].setPixmap(QtGui.QPixmap("3-box.png"))
        elif self.checkbomb[i][j] == 4:
            self.label[i][j].setPixmap(QtGui.QPixmap("4-box.png"))
        elif self.checkbomb[i][j] == 5:
            self.label[i][j].setPixmap(QtGui.QPixmap("5-box.png"))
        elif self.checkbomb[i][j] == 6:
            self.label[i][j].setPixmap(QtGui.QPixmap("6-box.png"))
        elif self.checkbomb[i][j] == 7:
            self.label[i][j].setPixmap(QtGui.QPixmap("7-box.png"))
        elif self.checkbomb[i][j] == 8:
            self.label[i][j].setPixmap(QtGui.QPixmap("8-box.png"))
        elif self.checkbomb[i][j] == "bomb":
            self.label[i][j].setPixmap(QtGui.QPixmap("bomb-box.png"))

    def pressed(self,i,j):
        self.button[i][j].hide()
        if self.checkbomb[i][j] == "bomb":
            self.flag = False
            self.Timertext.setText("You lost")
            font = QtGui.QFont()
            font.setPointSize(25)
            self.Timertext.setFont(font)
            self.checkbombs(i,j)
            self.label[i][j].setPixmap(QtGui.QPixmap("bomb-box.png"))
            for a in range(self.height):
                for b in range(self.width):
                    if self.checkbomb[a][b] == "bomb":
                        self.label[a][b].setPixmap(QtGui.QPixmap("bomb-box.png"))
                        self.button[a][b].hide()
                    else:
                        self.button[a][b].setEnabled(False)
        elif self.checkbomb[i][j] == 0:
            self.button[i][j].hide()
            self.spread(i,j)
        else:
            self.checkbombs(i,j)
            self.checkbomb[i][j] = "done"
        win = True
        for o in range(self.height):
            for p in range(self.width):
                if self.checkbomb[o][p] == "bomb" or self.checkbomb[o][p] == "done":
                    pass
                else:
                    win = False
                    break
        if win != False:
            self.flag = False
            MainWindow.hide()
            Winwindow.show()

    def subspread(self,i,j):
        try:
            if self.checkbomb[i][j] == 0:
                self.button[i][j].hide()
                self.checkbomb[i][j] = "done"
                self.spread(i,j)
            elif self.checkbomb[i][j] == "bomb":
                pass
            else:
                self.checkbombs(i,j)
                self.checkbomb[i][j] = "done"
                self.button[i][j].hide()
        except:
            pass

    def spread(self,i,j):
        self.checkbomb[i][j]="done"
        self.subspread(i-1,j-1)
        self.subspread(i-1,j)
        self.subspread(i-1,j+1)
        self.subspread(i,j-1)
        self.subspread(i,j+1)
        self.subspread(i+1,j-1)
        self.subspread(i+1,j)
        self.subspread(i+1,j+1)

    def exit(self):
        sys.exit(app.exec_())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minesweeper"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))

class WonWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 270, 161, 30))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(75, 20, 150, 150))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("source.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(25, 180, 250, 90))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 270, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Congratulation! \n","You won"))
        self.label_3.setText(_translate("MainWindow", "Place"))
        self.pushButton.setText(_translate("MainWindow", "Leaderboard"))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    thisMainWindow = QtWidgets.QMainWindow()
    GameWindow = QtWidgets.QMainWindow()
    Winwindow = QtWidgets.QMainWindow()
    ui = Main()
    game = MainWindow()
    winable = WonWindow()
    ui.setupUi(thisMainWindow)
    game.setupUi(GameWindow)
    winable.setupUi(Winwindow)
    thisMainWindow.show()
    sys.exit(app.exec_())