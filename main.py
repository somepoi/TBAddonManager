from PySide6.QtWidgets import QApplication, QMessageBox
from internal.interface import MainWindow, init_fonts
import sys, os
from pathlib import Path

from internal.lang import gt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    init_fonts()
    window = MainWindow()
    window.show()
    if not getattr(sys, 'frozen', False) or not os.path.exists(str(Path(sys.executable).parent / "lib" / "py3-windows-x86_64" / "python.exe")) or not os.path.exists(str(Path(sys.executable).parent / "TinyBunny_am.py")):
        QMessageBox.critical(window,
            gt("Error!"),
            gt("The program could not find Tiny Bunny game folder!"),
            QMessageBox.StandardButton.Ok
        )
    else:
        sys.exit(app.exec())
