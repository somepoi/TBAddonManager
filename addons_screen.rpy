# TODO: парс аватарки из стима по номеру аддона
# TODO: парс имени автора(ов) из стима по номеру аддона
# TODO: парс описания из стима по номеру аддона
# TODO: парс последней даты обновления
# TODO: заняться рефакторингом кода, пора переезжать на стили

init -999:

    if getattr(renpy.bootstrap, "tbam_initialized", False):

        
        style addons_button is main_menu_button:
            background "interface/button.png"
            hover_background "TBAddonManager/assets/images/button_hover.png"
            xminimum 438
            yminimum 86

        style addons_button_text is main_menu_button_text:
            color "#000"
            hover_color "#fff"
            text_align 0.5
            size 38
        
        style addons_inside_button is main_menu_button
        style addons_inside_button_text is main_menu_button_text

        screen addon_empty_state(title, subtitle):
            frame:
                xsize 1100
                ysize 540
                background None
                padding (15, 15)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 20

                    text _(title):
                        size 62
                        if preferences.language in ("japan", "chinese"):
                            font other_font_interface
                        else:
                            font "font/russia.ttf"
                        color "#666666"
                        xalign 0.5

                    text _(subtitle):
                        size 50
                        if preferences.language in ("japan", "chinese"):
                            font other_font_interface
                        else:
                            font "font/russia.ttf"
                        color "#555555"
                        xalign 0.5

        screen addon_info_placeholder(message):
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 30

                text "?":
                    size 240
                    color "#333333"
                    xalign 0.5
                    if preferences.language in ("japan", "chinese"):
                        font other_font_interface
                    else:
                        font "font/russia.ttf"

                text _(message):
                    if preferences.language in ("japan", "chinese"):
                        font other_font_interface
                    else:
                        font "font/russia.ttf"
                    size 50
                    color "#666666"
                    text_align 0.5
                    xalign 0.5

        screen addons:
            modal True
            tag menu
            style_prefix "addons"

            key "game_menu":
                action [SetField(tbam_store, "addon_search_query", ""), SetField(tbam_store, "selected_addon", ""), Return()]

            add gui.main_menu_background
            add "menu002_1"
            add "menu002_2"
            add "chastichka_2"
            add "menu001_1"
            add "menu001_2"
            add "chastichka_1_1"
            add "chastichka_1_2"
            add "bg_black" at mm_bg_diss_1to0

            vbox spacing 78:
                frame:
                    area(100, 80, 1720, 920)
                    background Solid("#000000cc")
                    padding (20, 20)

                    hbox:
                        spacing 20

                        # Левая панель - список аддонов
                        frame:
                            xsize 1100
                            ysize 880
                            background Solid("#00000099")
                            padding (15, 15)

                            vbox:
                                spacing 10

                                hbox:
                                    spacing 20
                                    xfill True

                                    text _("МЕНЕДЖЕР АДДОНОВ"):
                                        size 48
                                        color "#ffffff"
                                        if preferences.language in ("japan", "chinese"):
                                            font other_font_interface
                                        else:
                                            font "font/russia.ttf"

                                    null width 20

                                    if tbam_store.addons:
                                        # Такая реализация для правильной работы переводчика
                                        if tbam_store.addon_sort_reverse:
                                            $ sort_text = _("Сортировка: Я-А")
                                        else:
                                            $ sort_text = _("Сортировка: А-Я")
                                        
                                        textbutton sort_text:
                                            style_group "addons_inside_button"
                                            action Function(tbam_store.toggle_addon_sort)
                                            xalign 1.0
                                            yalign 0.5
                                            if preferences.language in ("japan", "chinese"):
                                                text_font other_font_interface
                                            else:
                                                text_font "font/russia.ttf"
                                            text_size 48
                                            text_idle_color "#aaaaaa"
                                            text_hover_color "#ffffff"

                                if tbam_store.addons:
                                    null height 15

                                    # Поисковая строка
                                    frame:
                                        xfill True
                                        background At(AlphaMask("#ffffff22", Frame("TBAddonManager/assets/images/mask.webp", Borders(30, 30, 30, 30))), Transform(alpha=0.65))
                                        padding (12, 8)
                                        xmaximum 1060

                                        hbox:
                                            spacing 12
                                            yalign 0.5

                                            add "TBAddonManager/assets/images/search_small.png" align(0.5, 0.5)

                                            hbox spacing 0:
                                                input:
                                                    value FieldInputValue(tbam_store, "addon_search_query")
                                                    length 100
                                                    allow None
                                                    size 40
                                                    color "#ffffff"
                                                    yalign 0.5
                                                    default ""
                                                    copypaste True

                                                if not tbam_store.addon_search_query:
                                                    text _("Поиск по названию, описанию или автору..."):
                                                        if preferences.language in ("japan", "chinese"):
                                                            font other_font_interface
                                                        else:
                                                            font "font/russia.ttf"
                                                        size 40
                                                        color "#666666"
                                                        yalign 0.5

                                    null height 10

                                    if tbam_store.addon_search_query:
                                        $ filtered_count = len(tbam_store.get_filtered_addons())
                                        text _("Найдено: [filtered_count]"):
                                            if preferences.language in ("japan", "chinese"):
                                                font other_font_interface
                                            else:
                                                font "font/russia.ttf"
                                            size 32
                                            color "#aaaaaa"
                                            xalign 0.0

                                    null height 5

                                    $ filtered_addons = tbam_store.get_filtered_addons()

                                    if filtered_addons:
                                        viewport id "addons_viewport":
                                            draggable True
                                            mousewheel True
                                            scrollbars "vertical"
                                            xsize 1060
                                            ysize 690

                                            vbox:
                                                spacing 8

                                                for label, addon in filtered_addons:
                                                    button:
                                                        xsize 1020
                                                        ysize 100
                                                        background Solid("#ffffff11")
                                                        hover_background Solid("#ffffff33")
                                                        hover_sound None
                                                        hovered [SetField(tbam_store, "selected_addon", addon)]
                                                        action Start(label)

                                                        hbox:
                                                            spacing 15
                                                            xalign 0.0
                                                            yalign 0.5

                                                            if addon.avatar:
                                                                add addon.avatar:
                                                                    size (80, 80)
                                                                    xalign 0.5
                                                                    yalign 0.5
                                                            else:
                                                                add "TBAddonManager/assets/images/avatar_placeholder.png" xsize 80 ysize 80

                                                            vbox:
                                                                spacing 5
                                                                yalign 0.5
                                                                xmaximum 900

                                                                text addon.get_truncated_name(60):
                                                                    size 40 
                                                                    color "#ffffff" 
                                                                    font "font/russia.ttf"
                                                                    xmaximum 900
                                                                    xalign 0.0

                                                                if addon.authors:
                                                                    text addon.get_authors():
                                                                        size 28
                                                                        color "#aaaaaa"
                                                                        xmaximum 900
                                                                        xalign 0.0
                                    else:
                                        use addon_empty_state("Ничего не найдено", "Попробуйте изменить поисковый запрос")
                                else:
                                    null height 100
                                    use addon_empty_state("Аддоны не найдены", "Установите аддоны в папку игры")

                        # Правая панель - информация о аддоне
                        frame:
                            xsize 560
                            ysize 880
                            background Solid("#00000099")
                            padding (15, 15)

                            if tbam_store.selected_addon:
                                vbox:
                                    spacing 20
                                    xfill True

                                    text _("ИНФОРМАЦИЯ ОБ АДДОНЕ"):
                                        size 48
                                        color "#ffffff"
                                        if preferences.language in ("japan", "chinese"):
                                            font other_font_interface
                                        else:
                                            font "font/russia.ttf"

                                    null height 10

                                    if tbam_store.selected_addon.avatar:
                                        frame:
                                            background None
                                            xalign 0.5
                                            padding (10, 10)
                                            xmaximum 256
                                            ymaximum 256
                                            
                                            add tbam_store.selected_addon.avatar:
                                                fit "contain"
                                                xalign 0.5
                                                yalign 0.5
                                    else:
                                        add "TBAddonManager/assets/images/avatar_placeholder.png" xsize 256 ysize 256 xalign 0.5

                                    null height 20

                                    text tbam_store.selected_addon.name:
                                        size tbam_store.selected_addon.get_adaptive_name_size()
                                        color "#ffffff"
                                        font "font/russia.ttf"
                                        xalign 0.5
                                        text_align 0.5
                                        xmaximum 500

                                    if tbam_store.selected_addon.authors:
                                        text tbam_store.selected_addon.get_authors():
                                            size 32
                                            color "#aaaaaa"
                                            xalign 0.5
                                            text_align 0.5
                                            xmaximum 500

                                    # чек, надо ли нам показывать скроллбар в зависимости от длины описания аддона
                                    python:
                                        import math
                                        desc_text = tbam_store.selected_addon.description
                                        chars_per_line = 50
                                        estimated_lines = math.ceil(len(desc_text) / chars_per_line)
                                        line_height = 24
                                        estimated_height = estimated_lines * line_height
                                        needs_scrollbar = estimated_height > 220

                                    frame:
                                        xfill True
                                        yfill True
                                        background Solid("#ffffff11")
                                        padding (15, 15)
                                        xmaximum 525
                                        ymaximum 500

                                        viewport id "description_viewport":
                                            draggable True
                                            mousewheel True
                                            scrollbars ("vertical" if needs_scrollbar else None)
                                            xsize 550
                                            yfill True

                                            text tbam_store.selected_addon.description:
                                                size 18
                                                font "font/GenEiAntiqueNv5-M.ttf"
                                                color "#dddddd"
                                                text_align 0.0
                                                xalign 0.0
                                                xmaximum 500
                            else:
                                if tbam_store.addons:
                                    use addon_info_placeholder("Выберите аддон из списка\nчтобы увидеть информацию")
                                else:
                                    use addon_info_placeholder("Установите аддоны\nчтобы увидеть информацию")
                
                textbutton _("Назад"):
                    xalign 0.5
                    action [SetField(tbam_store, "addon_search_query", ""), SetField(tbam_store, "selected_addon", ""), Return()]
