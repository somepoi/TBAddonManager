from typing import Optional
from locale import getdefaultlocale

lang = {
    "Tiny Bunny Addon Manager": {
        "ru_RU": "Менеджер Аддонов для игры Tiny Bunny"
    },
    "Developer mode": {
        "ru_RU": "Режим разработчика"
    },
    "In-game console": {
        "ru_RU": "Внутриигровая консоль"
    },
    "External console": {
        "ru_RU": "Внешняя консоль"
    },
    "Launch the game!": {
        "ru_RU": "Запустить игру!"
    },
    "Error!": {
        "ru_RU": "Ошибка!"
    },
    "The program could not find Tiny Bunny game folder!": {
        "ru_RU": "Программа не смогла найти папку игры Зайчик!"
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