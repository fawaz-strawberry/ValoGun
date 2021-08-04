import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtGui import QIcon, QFont
from threading import Timer
import time
import requests

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window'
        self.left = 100
        self.top = 100
        self.width = 1920
        self.height = 1080
        self.index = -1
        self.poses = ["crouch", "stand", "jump"]
        self.initUI()

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

        button = QPushButton('Start', self)
        button.setGeometry(self.width / 2 - 200, 70, 200, 200)
        button.setToolTip("Press to begin recording")
        button.clicked.connect(self.on_click)

        self.labelA = QLabel("Times font", self)
        self.labelA.setText('Pose Test')
        self.labelA.setGeometry(self.width / 2 - 900, self.height / 2 - 250, 1900, 500)
        self.labelA.setFont(QFont('Times', 100))

        self.show()


    @pyqtSlot()
    def on_click(self):

        def test_func():
            max_time = 3
            start_time = time.time()
            #Send Message to start recording
            while(time.time() - start_time < max_time):
                pass
            #Send Message to stop recording
            print("Finished Loop")

        print('Button Pressed')
        self.index += 1
        if(self.index >= len(self.poses)):
            exit(0)
        else:
            self.labelA.setText(self.poses[self.index])
        test_func()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


#Create list of different poses


#For each pose, ask user to do pose and then save video from camera
#with label of the pose. Connect with phone app to pull the video
#Use green screen and turn at different angles at slightly different heights


#Save into groups for aggregated data. 
