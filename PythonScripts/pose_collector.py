import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import pyqtSlot
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

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar.')

        # button = QPushButton('PyQt5 button', self)
        # button.setGeometry(100, 70, 200, 200)
        # button.setToolTip("This is the best button")
        # button.clicked.connect(self.on_click)

        labelA = QLabel("Times font", self)
        labelA.setText('Crouch')
        labelA.setGeometry(100, 70, 1800, 1000)
        labelA.setFont(QFont('Times', 100))

        self.show()


    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

#Create list of different poses
poses = ["crouch", "stand", "jump"]

#For each pose, ask user to do pose and then save video from camera
#with label of the pose. Connect with phone app to pull the video
#Use green screen and turn at different angles at slightly different heights


#Save into groups for aggregated data. 
