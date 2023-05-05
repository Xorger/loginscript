import subprocess
import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Window")
        layout = QGridLayout()
        coding_button = QPushButton("Coding")
        watching_button = QPushButton("Watching")
        cubing_button = QPushButton("Cubing")
        reading_button = QPushButton("Reading")
        layout.addWidget(coding_button, 0, 0)
        layout.addWidget(watching_button, 0, 1)
        layout.addWidget(cubing_button, 1, 0)
        layout.addWidget(reading_button, 1, 1)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        coding_button.clicked.connect(self.coding)
        watching_button.clicked.connect(self.watching)
        cubing_button.clicked.connect(self.cubing)
        reading_button.clicked.connect(self.reading)
    def coding(self):
        subprocess.Popen("emacs")
        subprocess.Popen(["qutebrowser", "stackoverflow.com"])
        time.sleep(3)
        subprocess.Popen(["qutebrowser", ":tab-give"])
        sys.exit()
    def watching(self):
        subprocess.Popen(["qutebrowser", "youtube.com"])
        time.sleep(3)
        subprocess.Popen(["qutebrowser", ":tab-give"])
        sys.exit()
    def cubing(self):
        subprocess.Popen(["qutebrowser", "jperm.net"])
        time.sleep(3)
        subprocess.Popen(["qutebrowser", ":tab-give"])
        time.sleep(3)
        subprocess.Popen(["qutebrowser", "cstimer.net"])
        time.sleep(3)
        subprocess.Popen(["qutebrowser", ":tab-give"])
        sys.exit()
    def reading(self):
        subprocess.Popen(["qutebrowser", "127.0.0.1:8080"])
        time.sleep(3)
        subprocess.Popen(["qutebrowser", ":tab-give"])
        sys.exit()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
