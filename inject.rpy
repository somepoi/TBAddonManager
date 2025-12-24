init -1000 python hide:
    from configparser import ConfigParser
    if "TBAddonManager.ini" in renpy.list_files():
        ini = ConfigParser()
        ini.read_string(renpy.file("TBAddonManager.ini").read().decode())
        if bool(int(ini.get("gameconfig", "enabled", fallback="0"))):
            renpy.bootstrap.tbam_initialized = True
        if bool(int(ini.get("gameconfig", "developer", fallback="0"))):
            renpy.bootstrap.tbam_developer = True
        if bool(int(ini.get("gameconfig", "console", fallback="0"))):
            renpy.bootstrap.tbam_console = True

init 1000 python:
    if getattr(renpy.bootstrap, "tbam_initialized", False):
        config.developer = getattr(renpy.bootstrap, "tbam_developer", config.developer)
        config.console = getattr(renpy.bootstrap, "tbam_console", config.console)
