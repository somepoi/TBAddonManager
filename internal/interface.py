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
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from pathlib import Path
import subprocess, sys, os

import internal.resources_rc
from internal.lang import gt
from internal.config import save, load

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
            QWidget { background-color: #1e1e1e; color: #dcdcdc; font-family: "Kazmann Sans"; font-size: 24px; }

            QPushButton { background-color: rgba(255,255,255,0.05); border: 4px outset rgba(32,32,32,1.0); padding: 8px 32px; }
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
        lbl.setStyleSheet("""
            QLabel { color: #dcdcdc; font-family: "Razor Keen"; font-size: 48px; }
        """)
        lbl.setText(gt("Tiny Bunny Addon Manager"))
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(lbl)

        # CheckBoxes
        layout_cb = QHBoxLayout()
        layout_cb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_cb.setSpacing(32)
        self.cb_enabled_by_default = QCheckBox()
        self.cb_developer = QCheckBox()
        self.cb_console = QCheckBox()
        self.cb_extconsole = QCheckBox()
        for var, text, tooltip in [
            (self.cb_developer,             gt("Developer mode"),                  gt("Game will have developer mode enabled (config.developer).")),
            (self.cb_console,               gt("In-game console"),                 gt("Game will have in-game console enabled (config.console).")),
            (self.cb_extconsole,            gt("External console"),                gt("Game will launch with external console enabled, allowing easier debugging of addons.")),
        ]:
            var.setText(text)
            var.setToolTip(tooltip)
            layout_cb.addWidget(var)
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

        config_values = load()

        self.cb_developer.setChecked(config_values[0])
        self.cb_console.setChecked(config_values[1])
        self.cb_extconsole.setChecked(config_values[2])

    def _start_game(self):

        save(self.cb_developer.isChecked(), self.cb_console.isChecked(), self.cb_extconsole.isChecked())

        args = [str(Path(sys.executable).parent / "lib" / "py3-windows-x86_64" / ("python.exe" if self.cb_extconsole.isChecked() else "pythonw.exe")), str(Path(sys.executable).parent / "TinyBunny.py")]

        self.process = GameRunner(self, args, self.cb_extconsole.isChecked())
        self.process.finished.connect(self._on_process_finished)
        self.hide()
        self.process.run()

    def _on_process_finished(self):
        self.show()

    def closeEvent(self, event: QEvent):
        save(self.cb_developer.isChecked(), self.cb_console.isChecked(), self.cb_extconsole.isChecked())
