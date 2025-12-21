from PySide6.QtCore import Qt, QEvent, QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtMultimedia import QSoundEffect
from .resources import get_resource
import os, base64

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(250, 250)
        self.setWindowTitle("fear me")

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.label = QLabel(self)
        pmap = QPixmap()
        pmap.load(get_resource("background.png"))
        self.label.setPixmap(pmap)
        self.label.setScaledContents(True)
        self.label.resize(self.size())
        self.label.lower()
        self.layout.addWidget(self.label)

        self.sound = QSoundEffect(self)
        self.sound.setSource(QUrl.fromLocalFile(get_resource("sound.wav")))

    def closeEvent(self, event: QEvent):
        self.sound.stop()
        self.sound.play()
        event.ignore()