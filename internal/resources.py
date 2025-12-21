from pathlib import Path
import sys

BASEPATH = Path(sys._MEIPASS) if hasattr(sys, "_MEIPASS") else Path(__file__).parent

get_resource = lambda name: str(BASEPATH / "resources" / name)
