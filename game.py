from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys,random,time,csv
class Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 360)
        MainWindow.setWindowIcon(QtGui.QIcon('bomb.png'))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.pressed(self.lineEdit.text(),self.lineEdit_2.text()))
        self.pushButton.setGeometry(QtCore.QRect(180, 240, 151, 71))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(18)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 50, 130, 40))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 140, 130, 40))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 240, 131, 61))
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
            if int(height) not in range(10,31) and int(width) not in range(10,31):
                self.label_3.setText("Please enter a\nheight and width\nin range of 10-30")
            elif int(height) not in range(10,31):
                self.label_3.setText("Please enter a height\nby number 10-30")
            elif int(width) not in range(10,31):
                self.label_3.setText("Please enter a width\nby number 10-30")
            elif int(height) in range(10,31):
                if int(width) in range(10,31):
                    game = MainWindow(int(height),int(width))
                    game.setupUi(GameWindow)
                    thisMainWindow.hide()
                    GameWindow.show()
        except:
            self.label_3.setText("Please enter a\nheight and width\nin range of 10-50")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minesweeper"))
        self.pushButton.setText(_translate("MainWindow", "Play now"))
        self.label.setText(_translate("MainWindow", "Height"))
        self.label_2.setText(_translate("MainWindow", "Width"))
        self.label_3.setText(_translate("MainWindow", "Please enter a\nheight and width\nin range of 10-50"))

class MainWindow(object):
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.label = []
        self.button = []
        self.mainheight = (25 * self.height) + 120
        self.mainwidth = (25 * self.width) + 40
        self.checkbomb = []
        self.timenow = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.mainwidth,self.mainheight)
        MainWindow.setWindowIcon(QtGui.QIcon('bomb.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        for m in range(self.height):
            self.label.append([])
            self.button.append([])
        y=100
        z=0
        for m in range(self.height):
            x=20
            for n in range(self.width):
                self.label[m].append(QtWidgets.QLabel(self.centralwidget))
                self.label[m][n].setGeometry(QtCore.QRect(x, y, 25, 25))
                self.label[m][n].setText("")
                self.label[m][n].setPixmap(QtGui.QPixmap("empty-box.png"))
                self.label[m][n].setScaledContents(True)
                self.label[m][n].setObjectName("label"+str(m)+"_"+str(n))
                self.button[m].append(QtWidgets.QPushButton(self.centralwidget))
                self.button[m][n].setGeometry(QtCore.QRect(x, y, 25, 25))
                self.button[m][n].setText("")
                self.button[m][n].setIcon(QIcon('empty-box.png'))
                self.button[m][n].setObjectName("button"+str(m)+"_"+str(n))
                self.button[m][n].clicked.connect(lambda checked, arg1 = m, arg2=n: self.pressed(arg1,arg2))
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
        self.Timertext.setText("0.0")
        self.count = 0
        self.flag = False
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
        self.resetButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.reset())
        self.resetButton.setGeometry(QtCore.QRect(25*self.width - 50, 20, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
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
            self.count += 1
            self.timenow = self.count / 10
            self.Timertext.setText(str(self.timenow))

    def checkbombs(self,m,n):
        if self.checkbomb[m][n] == 0:
            self.label[m][n].setPixmap(QtGui.QPixmap("empty-box.png"))
        elif self.checkbomb[m][n] == 1:
            self.label[m][n].setPixmap(QtGui.QPixmap("1-box.png"))
        elif self.checkbomb[m][n] == 2:
            self.label[m][n].setPixmap(QtGui.QPixmap("2-box.png"))
        elif self.checkbomb[m][n] == 3:
            self.label[m][n].setPixmap(QtGui.QPixmap("3-box.png"))
        elif self.checkbomb[m][n] == 4:
            self.label[m][n].setPixmap(QtGui.QPixmap("4-box.png"))
        elif self.checkbomb[m][n] == 5:
            self.label[m][n].setPixmap(QtGui.QPixmap("5-box.png"))
        elif self.checkbomb[m][n] == 6:
            self.label[m][n].setPixmap(QtGui.QPixmap("6-box.png"))
        elif self.checkbomb[m][n] == 7:
            self.label[m][n].setPixmap(QtGui.QPixmap("7-box.png"))
        elif self.checkbomb[m][n] == 8:
            self.label[m][n].setPixmap(QtGui.QPixmap("8-box.png"))
        elif self.checkbomb[m][n] == "bomb":
            self.label[m][n].setPixmap(QtGui.QPixmap("bomb-box.png"))

    def pressed(self,m,n):
        self.button[m][n].hide()
        if self.checkbomb == []:
            self.flag = True
            for x in range(self.height):
                self.checkbomb.append([])
                for y in range(self.width):
                    if m==x and n==y:
                        self.checkbomb[x].append(".")
                    else:
                        chance = random.randint(0, 100)
                        if chance < 20:
                            self.checkbomb[x].append("bomb")
                        else:
                            self.checkbomb[x].append(".")
            for x in range(self.height):
                for y in range(self.width):
                    if self.checkbomb[x][y] != "bomb":
                        bombs = 0
                        if x-1 >= 0:
                            if y-1 >= 0 and self.checkbomb[x-1][y-1] == "bomb":
                                bombs += 1
                            if self.checkbomb[x-1][y] == "bomb":
                                bombs += 1
                            if y+1 < self.width and self.checkbomb[x-1][y+1] == "bomb":
                                bombs += 1
                        if y-1 >= 0 and self.checkbomb[x][y-1] == "bomb":
                            bombs += 1
                        if y+1 < self.width and self.checkbomb[x][y+1] == "bomb":
                            bombs += 1
                        if x+1 < self.height:
                            if y-1 >= 0 and self.checkbomb[x+1][y-1] == "bomb":
                                bombs += 1
                            if self.checkbomb[x+1][y] == "bomb":
                                bombs += 1
                            if y+1 < self.width and self.checkbomb[x+1][y+1] == "bomb":
                                bombs += 1
                        self.checkbomb[x][y] = bombs
        if self.checkbomb[m][n] == "bomb":
            self.checkbombs(m,n)
            self.flag = False
            self.Timertext.setText("You lost")
            font = QtGui.QFont()
            font.setPointSize(25)
            self.Timertext.setFont(font)
            self.checkbombs(m,n)
            self.label[m][n].setPixmap(QtGui.QPixmap("bomb-box.png"))
            for a in range(self.height):
                for b in range(self.width):
                    if self.checkbomb[a][b] == "bomb":
                        self.label[a][b].setPixmap(QtGui.QPixmap("bomb-box.png"))
                        self.button[a][b].hide()
                    else:
                        self.button[a][b].setEnabled(False)
        elif self.checkbomb[m][n] == 0:
            self.checkbombs(m,n)
            self.button[m][n].hide()
            self.spread(m,n)
        else:
            self.checkbombs(m,n)
            self.checkbomb[m][n] = "done"
        win = True
        for o in range(self.height):
            for p in range(self.width):
                if self.checkbomb[o][p] == "bomb" or self.checkbomb[o][p] == "done":
                    pass
                else:
                    win = False
                    break
        if win:
            self.flag = False
            winable = WonWindow(self.timenow)
            winable.setupUi(Winwindow)
            GameWindow.hide()
            Winwindow.show()

    def subspread(self,m,n):
        if m in range(self.height) and n in range(self.width):
            if self.checkbomb[m][n] == 0:
                self.checkbombs(m,n)
                self.button[m][n].hide()
                self.checkbomb[m][n] = "done"
                self.spread(m,n)
            elif self.checkbomb[m][n] == "bomb":
                self.checkbombs(m,n)
            else:
                self.checkbombs(m,n)
                self.checkbomb[m][n] = "done"
                self.button[m][n].hide()

    def spread(self,m,n):
        self.checkbomb[m][n]="done"
        self.subspread(m-1,n-1)
        self.subspread(m-1,n)
        self.subspread(m-1,n+1)
        self.subspread(m,n-1)
        self.subspread(m,n+1)
        self.subspread(m+1,n-1)
        self.subspread(m+1,n)
        self.subspread(m+1,n+1)

    def reset(self):
        for i in range(self.height):
            for j in range(self.width):
                self.button[i][j].show()
                self.button[i][j].setEnabled(True)
        self.checkbomb = []
        self.flag = False
        self.count = 0
        self.Timertext.setText("0.0")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minesweeper"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))

class WonWindow(object):
    def __init__(self,time):
        self.time = str(time)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 350)
        MainWindow.setWindowIcon(QtGui.QIcon('bomb.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.movie = QMovie("hooray.gif")
        self.movie.start()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(75, 20, 150, 150))
        self.label.setText("")
        self.label.setMovie(self.movie)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Minesweeper"))
        self.label_2.setText(_translate("MainWindow", "Congratulation! \n","You won"))
        self.label_3.setText(_translate("MainWindow", self.time + " seconds"))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    thisMainWindow = QtWidgets.QMainWindow()
    GameWindow = QtWidgets.QMainWindow()
    Winwindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(thisMainWindow)
    thisMainWindow.show()
    sys.exit(app.exec_())