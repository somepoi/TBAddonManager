# TODO: парс аватарки из стима по номеру аддона
# TODO: парс имени автора(ов) из стима по номеру аддона
# TODO: парс описания из стима по номеру аддона
# TODO: парс последней даты обновления

init -999:

    if getattr(renpy.bootstrap, "tbam_initialized", False):
        screen addon_empty_state(title, subtitle):
            style_prefix "addons_empty"
            
            frame:
                vbox:
                    text _(title):
                        style "addons_empty_title_text"

                    text _(subtitle):
                        style "addons_empty_subtitle_text"

        screen addon_info_placeholder(message):
            style_prefix "addons_placeholder"
            
            vbox:
                text "?":
                    style "addons_placeholder_icon_text"

                text _(message):
                    style "addons_placeholder_message_text"

        screen addons:
            modal True
            tag menu

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

            vbox:
                style "addons_outer_vbox"
                
                frame:
                    style "addons_main_container"

                    hbox:
                        style "addons_main_hbox"

                        frame:
                            style "addons_left_panel"

                            vbox:
                                style "addons_main_vbox"

                                hbox:
                                    style "addons_header_hbox"

                                    text _("МЕНЕДЖЕР АДДОНОВ"):
                                        style "addons_header_text"

                                    null width 20

                                    if tbam_store.addons:
                                        if tbam_store.addon_sort_reverse:
                                            $ sort_text = _("Сортировка: Я-А")
                                        else:
                                            $ sort_text = _("Сортировка: А-Я")
                                        
                                        textbutton sort_text:
                                            style "addons_sort_button"
                                            action Function(tbam_store.toggle_addon_sort)
                                            align (1.0, 0.5)

                                if tbam_store.addons:
                                    null height 15

                                    frame:
                                        style "addons_search_frame"

                                        hbox:
                                            style "addons_search_hbox"

                                            add "TBAddonManager/assets/images/search_small.png" align(0.5, 0.5)

                                            hbox style "addons_search_input_hbox":
                                                input:
                                                    style "addons_search_input"
                                                    value FieldInputValue(tbam_store, "addon_search_query")
                                                    length 100
                                                    allow None
                                                    default ""
                                                    copypaste True

                                                if not tbam_store.addon_search_query:
                                                    text _("Поиск по названию, описанию или автору..."):
                                                        style "addons_search_placeholder_text"

                                    null height 10
                                    
                                    $ filtered_addons = tbam_store.get_filtered_addons()
                                    $ filtered_count = len(filtered_addons)

                                    if tbam_store.addon_search_query:
                                        text _("Найдено: [filtered_count]"):
                                            style "addons_counter_text"

                                    null height 5

                                    if filtered_addons:
                                        viewport:
                                            style "addons_list_viewport"
                                            id "addons_viewport"
                                            draggable True
                                            mousewheel True
                                            scrollbars ("vertical" if filtered_count > 6 else None)

                                            vbox:
                                                style "addons_list_vbox"

                                                for label, addon in filtered_addons:
                                                    button:
                                                        style "addons_list_item_button"
                                                        hovered [SetField(tbam_store, "selected_addon", addon)]
                                                        action Start(label)

                                                        hbox:
                                                            style "addons_list_item_hbox"

                                                            if addon.avatar:
                                                                add addon.avatar:
                                                                    xysize(80, 80)
                                                                    align(0.5, 0.5)
                                                            else:
                                                                add "TBAddonManager/assets/images/avatar_placeholder.png":
                                                                    xysize(80, 80)
                                                                    align(0.5, 0.5)

                                                            vbox:
                                                                style "addons_list_item_vbox"

                                                                text addon.get_truncated_name(60):
                                                                    style "addons_list_item_name_text"

                                                                if addon.authors:
                                                                    text addon.get_authors():
                                                                        style "addons_list_item_author_text"
                                    else:
                                        use addon_empty_state("Ничего не найдено", "Попробуйте изменить поисковый запрос")
                                else:
                                    null height 100
                                    use addon_empty_state("Аддоны не найдены", "Установите аддоны в папку игры")

                        frame:
                            style "addons_right_panel"

                            if tbam_store.selected_addon:
                                vbox:
                                    style "addons_info_vbox"

                                    text _("ИНФОРМАЦИЯ ОБ АДДОНЕ"):
                                        style "addons_info_header_text"

                                    null height 10

                                    if tbam_store.selected_addon.avatar:
                                        frame:
                                            style "addons_info_avatar_frame"
                                            
                                            add tbam_store.selected_addon.avatar:
                                                fit "contain"
                                                xalign 0.5
                                                yalign 0.5
                                    else:
                                        add "TBAddonManager/assets/images/avatar_placeholder.png" xsize 256 ysize 256 xalign 0.5

                                    null height 20

                                    text tbam_store.selected_addon.name:
                                        style "addons_info_name_text"
                                        size tbam_store.selected_addon.get_adaptive_name_size()

                                    if tbam_store.selected_addon.authors:
                                        text tbam_store.selected_addon.get_authors():
                                            style "addons_info_author_text"

                                    python:
                                        import math
                                        desc_text = tbam_store.selected_addon.description
                                        chars_per_line = 50
                                        estimated_lines = math.ceil(len(desc_text) / chars_per_line)
                                        line_height = 24
                                        estimated_height = estimated_lines * line_height
                                        needs_scrollbar = estimated_height > 220

                                    frame:
                                        style "addons_info_desc_frame"

                                        viewport:
                                            style "addons_info_desc_viewport"
                                            id "description_viewport"
                                            draggable True
                                            mousewheel True
                                            scrollbars ("vertical" if needs_scrollbar else None)

                                            text tbam_store.selected_addon.description:
                                                style "addons_info_desc_text"
                            else:
                                if tbam_store.addons:
                                    use addon_info_placeholder("Выберите аддон из списка\nчтобы увидеть информацию")
                                else:
                                    use addon_info_placeholder("Установите аддоны\nчтобы увидеть информацию")
                
                textbutton _("Назад"):
                    style "addons_button"
                    xalign 0.5
                    action [SetField(tbam_store, "addon_search_query", ""), SetField(tbam_store, "selected_addon", ""), Return()]
