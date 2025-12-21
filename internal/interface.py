from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from .resources import get_resource

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(600, 300)
        self.setWindowTitle("Addon Manager")
        self.setStyleSheet("""
            QWidget { background-color: #1e1e1e; color: #dcdcdc; }
            """)
