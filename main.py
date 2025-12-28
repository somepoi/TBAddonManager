from PySide6.QtWidgets import QApplication, QMessageBox, QFileDialog
from internal.interface import MainWindow, init_fonts
import sys, os
from pathlib import Path

from internal.lang import gt
import internal.config

if __name__ == "__main__":
    app = QApplication(sys.argv)
    init_fonts()
    internal.config.working_path = QFileDialog.getExistingDirectory(None, "tiny bunny folder") if not getattr(sys, 'frozen', False) else str(Path(sys.executable).parent)
    window = MainWindow()
    if not os.path.exists(str(Path(internal.config.working_path) / "lib" / "py3-windows-x86_64" / "python.exe")) or not os.path.exists(str(Path(internal.config.working_path) / "TinyBunny.py")):
        QMessageBox.critical(window,
            gt("Error!"),
            gt("The program could not find Tiny Bunny game folder!"),
            QMessageBox.StandardButton.Ok
        )
    else:
        window.show()
        sys.exit(app.exec())
