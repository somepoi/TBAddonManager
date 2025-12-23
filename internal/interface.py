from PySide6.QtCore import (
    QEvent,
    QStandardPaths,
    QThread,
    Qt,
    Signal,
)
from PySide6.QtGui import (
    QFontDatabase,
    QIcon,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
import subprocess, pathlib, sys, os

import internal.resources_rc
from internal.lang import gt

def init_fonts():
    fonts = {}
    for name in [
        ":/font/title.ttf",
        ":/font/body.ttf",
    ]:
        fonts[name] = QFontDatabase.addApplicationFont(name)
        if fonts[name] != -1:
            print(f"Loaded font \"{name}\" with names {QFontDatabase.applicationFontFamilies(fonts[name])}")
        else:
            print(f"Could not find font \"{name}\"!")

class GameRunner(QThread):
    finished = Signal()

    def __init__(self, parent, args, visible):
        super().__init__(parent)
        self.args = args
        self.visible = visible

    def run(self):
        subprocess.run(self.args, creationflags=subprocess.CREATE_NEW_CONSOLE if self.visible else subprocess.CREATE_NO_WINDOW)
        self.finished.emit()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(gt("Tiny Bunny Addon Manager"))
        self.setWindowIcon(QIcon(":/img/icon.ico"))
        self.setStyleSheet("""
            QWidget { background-color: #1e1e1e; color: #dcdcdc; font-family: "Kazmann Sans"; font-size: 36px; }
            QLabel { color: #dcdcdc; font-family: "Razor Keen"; font-size: 64px; }

            QPushButton { background-color: rgba(255,255,255,0.05); border: 4px outset rgba(32,32,32,1.0); padding: 16px 64px; }
            QPushButton:hover { background-color: rgba(255,255,255,0.15); border: 4px outset rgba(32,32,32,1.0); }
            QPushButton:pressed { background-color: rgba(255,255,255,0.05); border: 4px inset rgba(32,32,32,1.0); }
            """)

        # Main Layout and Logo
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.setContentsMargins(64,32,64,32)
        self.main_layout.setSpacing(8)

        lbl = QLabel(self)
        lbl.setText(gt("Tiny Bunny Addon Manager"))
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(lbl)

        # CheckBoxes
        layout_cb = QHBoxLayout()
        layout_cb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_cb.setSpacing(32)
        self.cb_dev = QCheckBox(gt("Developer mode"))
        self.cb_console = QCheckBox(gt("In-game console"))
        self.cb_debug = QCheckBox(gt("External console"))
        layout_cb.addWidget(self.cb_dev)
        layout_cb.addWidget(self.cb_console)
        layout_cb.addWidget(self.cb_debug)
        self.main_layout.addLayout(layout_cb)
        self.main_layout.addSpacing(8)

        # Buttons
        layout_btn = QHBoxLayout()
        layout_btn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_start = QPushButton(gt("Launch the game!"))
        self.btn_start.clicked.connect(self._start_game)
        layout_btn.addWidget(self.btn_start)
        self.main_layout.addLayout(layout_btn)

        self.setFixedSize(self.layout().sizeHint())

    def _start_game(self):

        gamefolder = str(pathlib.Path(sys.executable).parent) if getattr(sys, 'frozen', False) else QFileDialog.getExistingDirectory(self, "Select the path to the game folder", QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation), QFileDialog.Option.ShowDirsOnly)
        if not os.path.exists(str(pathlib.Path(gamefolder) / "lib" / "py3-windows-x86_64" / "python.exe")) or not os.path.exists(str(pathlib.Path(gamefolder) / "TinyBunny_am.py")):
            QMessageBox.critical(self,
                    gt("Error!"),
                    gt("The program could not find Tiny Bunny game folder!"),
                    QMessageBox.StandardButton.Ok
            )
            return

        args = [str(pathlib.Path(gamefolder) / "lib" / "py3-windows-x86_64" / ("python.exe" if self.cb_debug.isChecked() else "pythonw.exe")), str(pathlib.Path(gamefolder) / "TinyBunny_am.py"), "-addon-manager"]
        if self.cb_console:
            args.append("-console")
        if self.cb_dev:
            args.append("-developer")

        self.process = GameRunner(self, args, self.cb_debug.isChecked())
        self.process.finished.connect(self._on_process_finished)
        self.hide()
        self.process.run()

    def _on_process_finished(self):
        self.show()
