import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Timetable Generator")
        button = QPushButton("Click me!")
        button.setCheckable(True)
        button.clicked.connect(self.isClick)
        self.setCentralWidget(button)

    def  isClick(self):
        print("Clicked...")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()