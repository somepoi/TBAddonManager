# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    excludes=[
        "PySide6.QtWebEngineWidgets*",
        "PySide6.QtWebEngineCore*",
        "PySide6.QtWebEngineQuick*",
        "PySide6.QtMultimedia*",
        "PySide6.QtMultimediaWidgets*",
        "PySide6.QtSvg*",
        "PySide6.QtSvgWidgets*",
        "PySide6.QtOpenGL*",
        "PySide6.QtOpenGLWidgets*",
        "PySide6.Qt3DCore*",
        "PySide6.Qt3DRender*",
        "PySide6.Qt3DInput*",
        "PySide6.QtCharts*",
        "PySide6.QtLocation*",
        "PySide6.QtPositioning*",
        "PySide6.QtSensors*",
        "PySide6.QtTextToSpeech*",
        "PySide6.QtNetworkAuth*",
        "PySide6.QtRemoteObjects*",
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='launcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)