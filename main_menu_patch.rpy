init 1:
    screen main_menu():
        tag menu
        style_prefix "main_menu"



        add gui.main_menu_background
        if persistent.animal_unlock[3]:
            add "interface/main_meny/fon_05.png"
        if persistent.animal_unlock[0]:
            add "interface/main_meny/fon_02.png"
        if persistent.animal_unlock[4]:
            add "interface/main_meny/fon_06.png"
        add "menu002_1"
        add "menu002_2"
        add "chastichka_2"
        if persistent.animal_unlock[1]:
            add "interface/main_meny/fon_03.png"
        if persistent.animal_unlock[2]:
            add "interface/main_meny/fon_04.png"
        add "menu001_1"
        add "menu001_2"
        add "chastichka_1_1"
        add "main_menu_bg"
        add "chastichka_1_2"

        add "bg_black" at mm_bg_diss_1to0


        if preferences.language != "japan":
            add "[logo!t]" xalign 0.47 yalign 0.09 at mm_elements
        else:
            add "interface/main_meny/logo_en.png" xalign 0.47 yalign 0.09 at mm_elements

        on "show" action ShowTransient(lang_mm_screen[preferences.language])
        on "replace" action ShowTransient(lang_mm_screen[preferences.language])
        on "replaced" action Hide(lang_mm_screen[preferences.language])
        on "hide" action Hide(lang_mm_screen[preferences.language])


        fixed:
            xfit True
            yfit True

            ypos 100

            at mm_elements
            hbox:
                xpos 80
                ypos 100
                button:
                    xsize 103
                    ysize 192
                    background "interface/main_meny/lapka_01.png"
                    if preferences.language != None:
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    activate_sound "sounds/menu/language-sellect-1.ogg"
                    action Language(None)
                    hovered ShowTransient("main_menu_language_message_rus")
                    unhovered ShowTransient(lang_mm_screen[preferences.language])
                    text "РУС":
                        xpos 40
                        ypos 105
                        font "font/razor_k.ttf"
                        color "000000"
                        size 40
                    at mm_but_lang
                at mm_elements

            hbox:

                xpos 180
                ypos 200
                button:
                    xsize 103
                    ysize 192
                    background "interface/main_meny/lapka_02.png"
                    if preferences.language != "english":
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    activate_sound "sounds/menu/language-sellect-1.ogg"
                    action Language("english")
                    hovered ShowTransient("main_menu_language_message_eng")
                    unhovered ShowTransient(lang_mm_screen[preferences.language])
                    text "ENG":
                        xpos 35
                        ypos 105
                        font "font/razor_k.ttf"
                        color "000000"
                        size 40
                    at mm_but_lang
                at mm_elements

            hbox:

                xpos 80
                ypos 300
                button:
                    xsize 103
                    ysize 192
                    background "interface/main_meny/lapka_04.png"
                    if preferences.language != "chinese":
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    activate_sound "sounds/menu/language-sellect-1.ogg"
                    action Language("chinese")
                    hovered ShowTransient("main_menu_language_message_chi")
                    unhovered ShowTransient(lang_mm_screen[preferences.language])
                    at mm_but_lang
                at mm_elements

            hbox:

                xpos 180
                ypos 400
                button:
                    xsize 103
                    ysize 192
                    background "interface/main_meny/lapka_02.png"
                    if preferences.language != "italiano":
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    activate_sound "sounds/menu/language-sellect-1.ogg"
                    action Language("italiano")
                    hovered ShowTransient("main_menu_language_message_ita")
                    unhovered ShowTransient(lang_mm_screen[preferences.language])
                    text "ITA":
                        xpos 35
                        ypos 105
                        font "font/razor_k.ttf"
                        color "000000"
                        size 40
                    at mm_but_lang
                at mm_elements

            hbox:

                xpos 80
                ypos 500
                button:
                    xsize 103
                    ysize 192
                    background "interface/main_meny/lapka_01.png"
                    if preferences.language != "turkish":
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    activate_sound "sounds/menu/language-sellect-1.ogg"
                    action Language("turkish")
                    hovered ShowTransient("main_menu_language_message_tur")
                    unhovered ShowTransient(lang_mm_screen[preferences.language])
                    text "TÜR":
                        xalign .5
                        xoffset 5
                        ypos 105
                        font "font/razor_k.ttf"
                        color "000000"
                        size 40
                    at mm_but_lang
                at mm_elements

            hbox:

                xpos 180
                ypos 600
                button:
                    xsize 103
                    ysize 192
                    background "interface/main_meny/lapka_02.png"
                    if preferences.language != "japan":
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    activate_sound "sounds/menu/language-sellect-1.ogg"
                    action Language("japan")
                    hovered ShowTransient("main_menu_language_message_jpn")
                    unhovered ShowTransient(lang_mm_screen[preferences.language])

                    text "JPN":
                        xalign .5
                        xoffset -5
                        ypos 105
                        font "font/razor_k.ttf"
                        color "000000"
                        size 40
                    at mm_but_lang
                at mm_elements

        vbox:
            xalign 0.47
            yalign 0.4
            textbutton _("Новая игра"):
                action Show("black_screen")
                if preferences.language == "japan":
                    text_font other_font_interface
                keyboard_focus False
            textbutton _("Загрузить"):
                action ShowMenu("load")
                if preferences.language == "japan":
                    text_font other_font_interface
                keyboard_focus False
            textbutton _("Настройки"):
                action ShowMenu("preferences")
                if preferences.language == "japan":
                    text_font other_font_interface
                keyboard_focus False
            textbutton _("Аддоны"):
                action ShowMenu("addons")
                if preferences.language == "japan":
                    text_font other_font_interface
                keyboard_focus False
            textbutton _("Об авторах"):
                action ShowMenu("about_me")
                if preferences.language == "japan":
                    text_font other_font_interface
                keyboard_focus False
            textbutton _("Выход"):
                action Quit(confirm=False)
                if preferences.language == "japan":
                    text_font other_font_interface
                keyboard_focus False
            at mm_elements


        vbox:
            xalign 0.47
            yalign 0.4
            button:
                background "interface/main_meny/plaska.png"
                text _("Новая игра"):
                    if preferences.language == "japan":
                        font other_font_interface
                at mm_but
                action Show("black_screen")
                default_focus True
            button:
                background "interface/main_meny/plaska.png"
                text _("Загрузить"):
                    if preferences.language == "japan":
                        font other_font_interface
                at mm_but
                action ShowMenu("load")
            button:
                background "interface/main_meny/plaska.png"
                text _("Настройки"):
                    if preferences.language == "japan":
                        font other_font_interface
                at mm_but
                action ShowMenu("preferences")
            button:
                background "interface/main_meny/plaska.png"
                text _("Аддоны"):
                    if preferences.language == "japan":
                        font other_font_interface
                at mm_but
                action ShowMenu("addons")
            button:
                background "interface/main_meny/plaska.png"
                text _("Об авторах"):
                    if preferences.language == "japan":
                        font other_font_interface
                at mm_but
                action ShowMenu("about_me")
            button:
                background "interface/main_meny/plaska.png"
                text _("Выход"):
                    if preferences.language == "japan":
                        font other_font_interface
                at mm_but
                action Quit(confirm=False)
            at mm_elements

        key "game_menu" action Quit(confirm=True)

        if not config.developer:
            on "show" action Show("block_screen")
            timer 3.2 action Hide("block_screen")

        if config.developer:
            use devolver_menu()