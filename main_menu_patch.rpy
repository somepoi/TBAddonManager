screen main_menu_addons:
    tag menu
    style_prefix "main_menu"

    use main_menu

    imagebutton:
        auto "TBAddonManager/assets/images/logo_%s.png"
        hover_sound "sounds/menu/menu-button-select-3.ogg"
        activate_sound "sounds/menu/language-sellect-1.ogg"
        xalign 0.95
        yalign 0.95
        action ShowMenu("addons", _transition=Fade(0.0, 0.0, 0.5))
        at mm_elements

label main_menu_addons:

    call screen main_menu_addons
    return
