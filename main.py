from PySide6.QtWidgets import QApplication
from internal.interface import MainWindow, init_fonts
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    init_fonts()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())