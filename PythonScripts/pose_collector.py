import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtGui import QIcon, QFont

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window'
        self.left = 100
        self.top = 100
        self.width = 1920
        self.height = 1080
        self.initUI()
        self.i = 0
        self.poses = ["crouch", "stand", "jump"]

    @pyqtSlot()
    def update_label(self):
        print("Updating")
        self.labelA.setText(self.poses[self.i])
        self.i += 1
        if(self.i >= len(self.poses)):
            self.i = 0
        self.labelA.setFont(QFont('Times', 100))

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar.')


        self.labelA = QLabel("Arial", self)
        self.labelA.setGeometry(100, 70, 1800, 1000)

        button = QPushButton('Start Collect', self)
        button.setGeometry(self.width / 2 - 200, 70, 200, 200)
        button.setToolTip("Begin Data Collection")
        button.clicked.connect(self.on_click)

        timer = QTimer()
        timer.timeout.connect(self.update_label)
        timer.start(1000)


        self.show()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


#Create list of different poses


#For each pose, ask user to do pose and then save video from camera
#with label of the pose. Connect with phone app to pull the video
#Use green screen and turn at different angles at slightly different heights


#Save into groups for aggregated data. 
