from configparser import ConfigParser
import sys
from pathlib import Path

def save(developer: bool, console: bool, extconsole: bool):
    ini = ConfigParser()
    ini.add_section("gameconfig")
    ini["gameconfig"]["enabled"] = "1"
    ini["gameconfig"]["developer"] = str(int(developer))
    ini["gameconfig"]["console"] = str(int(console))
    ini["gameconfig"]["extconsole"] = str(int(extconsole))
    with open(Path(sys.executable).parent / "game" / "TBAddonManager.ini", "w+") as file:
        ini.write(file)

def load():
    ini = ConfigParser()
    ini.read(Path(sys.executable).parent / "game" / "TBAddonManager.ini")
    try:
        return [bool(int(ini["gameconfig"][i])) for i in ["developer", "console", "extconsole"]]
    except Exception as e:
        return [False, False, False]
