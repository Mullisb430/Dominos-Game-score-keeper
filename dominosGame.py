import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class Dominos(QMainWindow):
    def __init__(self):
        super(Dominos, self).__init__()
        loadUi('dominosGUI.ui', self)
        self.winningColor = "color: rgb(40, 207, 40)"
        self.losingColor = "color: rgb(207, 40, 40)"
        self.phillyScore_ = [0]
        self.brandonScore_ = [0]
        self.loggedScore = ['', '', '', '', '', '', '', '']
        self.brandonButton.clicked.connect(self.addPoints)
        self.phillyButton.clicked.connect(self.addPoints)
        self.brandonAddPoints.returnPressed.connect(self.addPoints)
        self.phillyAddPoints.returnPressed.connect(self.addPoints)
        self.brandonButton.clicked.connect(self.logScore)
        self.phillyButton.clicked.connect(self.logScore)
        self.brandonAddPoints.returnPressed.connect(self.logScore)
        self.phillyAddPoints.returnPressed.connect(self.logScore)
        self.brandonButton.clicked.connect(self.color)
        self.phillyButton.clicked.connect(self.color)
        self.brandonAddPoints.returnPressed.connect(self.color)
        self.phillyAddPoints.returnPressed.connect(self.color)
        self.resetButton.clicked.connect(self.reset)

    def addPoints(self):
        try:
            self.brandonScore_.append(int(self.brandonAddPoints.text()))
            if (self.brandonAddPoints.text()) != '0':
                if int(self.brandonAddPoints.text()) > 0:
                    self.loggedScore.append(f"Brandon: +{self.brandonAddPoints.text()}")
                elif int(self.brandonAddPoints.text()) < 0:
                    self.loggedScore.append(f"Brandon: {self.brandonAddPoints.text()}")
        except:
            self.brandonScore_.append(0)
        try:
            self.phillyScore_.append(int(self.phillyAddPoints.text()))
            if (self.phillyAddPoints.text()) != '0':
                if int(self.phillyAddPoints.text()) > 0:
                    self.loggedScore.append(f"Philly: +{self.phillyAddPoints.text()}")
                elif int(self.phillyAddPoints.text()) < 0:
                    self.loggedScore.append(f"Philly {self.phillyAddPoints.text()}")
        except:
            self.phillyScore_.append(0)


        self.brandonScore.setText(str(sum(self.brandonScore_)))
        self.phillyScore.setText(str(sum(self.phillyScore_)))

        self.phillyAddPoints.setText('')
        self.brandonAddPoints.setText('')

    def logScore(self):
        self.lastScore.setText(f"Last score: {self.loggedScore[-1]}")
        self.secondScore.setText(self.loggedScore[-2])
        self.thirdScore.setText(self.loggedScore[-3])
        self.fourthScore.setText(self.loggedScore[-4])
        self.fifthScore.setText(self.loggedScore[-5])
        self.sixthScore.setText(self.loggedScore[-6])
        self.seventhScore.setText(self.loggedScore[-7])
        self.eighthScore.setText(self.loggedScore[-8])

    def color(self):
        try:
            if int(self.brandonScore.text()) >  int(self.phillyScore.text()):
                self.label.setStyleSheet(self.winningColor)
                self.label_2.setStyleSheet(self.losingColor)
            elif int(self.brandonScore.text()) <  int(self.phillyScore.text()):
                self.label.setStyleSheet(self.losingColor)
                self.label_2.setStyleSheet(self.winningColor)
            elif int(self.brandonScore.text()) == int(self.phillyScore.text()):
                self.label.setStyleSheet("color: rgb(209, 207, 212)")
                self.label_2.setStyleSheet("color: rgb(209, 207, 212)")
        except:
            self.label.setStyleSheet("color: rgb(209, 207, 212)")
            self.label_2.setStyleSheet("color: rgb(209, 207, 212)")

    def reset(self):
        self.phillyScore_ = [0]
        self.brandonScore_ = [0]
        self.loggedScore = ['', '', '', '', '', '', '', '']
        self.lastScore.setText('')
        self.secondScore.setText('')
        self.thirdScore.setText('')
        self.fourthScore.setText('')
        self.fifthScore.setText('')
        self.sixthScore.setText('')
        self.seventhScore.setText('')
        self.eighthScore.setText('')
        self.brandonScore.setText('0')
        self.phillyScore.setText('0')



app = QApplication(sys.argv)
dominos = Dominos()
dominos.show()
dominos.setFixedSize(800, 658)
app.exec_()