from typing import Optional
from locale import getdefaultlocale

lang = {
    "Tiny Bunny Addon Manager": {
        "ru_RU": "Менеджер Аддонов для игры Tiny Bunny"
    }
}

def get_translated(s: str, locale: Optional[str] = None) -> str:
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