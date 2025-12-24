from typing import Optional
from locale import getdefaultlocale

lang = {
    "Tiny Bunny Addon Manager": {
        "ru_RU": "Менеджер аддонов для игры Tiny Bunny"
    },
    "Developer mode": {
        "ru_RU": "Режим разработчика"
    },
    "Game will have developer mode enabled (config.developer).": {
        "ru_RU": "В игре будет включён режим разработчика (config.developer)."
    },
    "In-game console": {
        "ru_RU": "Внутриигровая консоль"
    },
    "Game will have in-game console enabled (config.console).": {
        "ru_RU": "В игре будет включена внутриигровая консоль (config.console)."
    },
    "External console": {
        "ru_RU": "Внешняя консоль"
    },
    "Game will launch with external console enabled, allowing easier debugging of addons.": {
        "ru_RU": "Игра будет запущена с внешней консолью, что упростит отладку аддонов."
    },
    "Launch the game!": {
        "ru_RU": "Запустить игру!"
    },
    "Error!": {
        "ru_RU": "Ошибка!"
    },
    "The program could not find Tiny Bunny game folder!": {
        "ru_RU": "Программа не смогла найти папку игры Tiny Bunny!"
    }
}

def gt(s: str, locale: Optional[str] = None) -> str:
    """
    Translates string `s` to `locale` language or falls back to the original `s` if no translation found.
    Args:
        s: Original string.
        locale: Target locale string. Defaults to computer's locale.
    Returns:
        Translated or untranslated string `s`.
    """
    if locale is None:
        locale = getdefaultlocale()[0]
    if not s in lang:
        print(f"Could not find string \"{s}\" in lang.")
        return s
    localized = lang[s]
    return localized.get(locale, s)
