# TODO: парс аватарки из стима по номеру мода
# TODO: парс имени автора(ов) из стима по номеру мода
# TODO: парс описания из стима по номеру мода
# TODO: парс последней даты обновления
# TODO: починить пустое пространство у описания мода в правой панели
# TODO: починить прыжки описания мода в правой панели из-за смены размера шрифта имени мода
# TODO: починить вывод "ничего не найдено"
# TODO: починить вывод "моды не установлены"
# TODO: заменить кнопку "назад"

screen addons:
    modal True 
    tag menu
    style_prefix "main_menu"

    key "game_menu":
        action Return()
    
    add gui.main_menu_background
    add "menu002_1"
    add "menu002_2"
    add "chastichka_2"
    add "menu001_1"
    add "menu001_2"
    add "chastichka_1_1"
    add "chastichka_1_2"
    add "bg_black" at mm_bg_diss_1to0

    vbox spacing 90:
        if addons:
            frame:
                area(100, 80, 1720, 920)
                background Solid("#000000cc")
                padding (20, 20)
                
                hbox:
                    spacing 20
                    
                    # список модов
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
                                
                                text "МЕНЕДЖЕР АДДОНОВ" size 48 color "#ffffff" font "font/russia.ttf" 
                                
                                null width 20
                                
                                textbutton ("{size=48}Сортировка: " + ("Я-А" if addon_sort_reverse else "А-Я") + "{/size}"):
                                    action Function(toggle_addon_sort)
                                    xalign 1.0
                                    yalign 0.5
                                    text_font "font/russia.ttf" 
                                    text_idle_color "#aaaaaa"
                                    text_hover_color "#ffffff"
                            
                            null height 15
                            
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
                                            value VariableInputValue("addon_search_query")
                                            length 100
                                            allow None
                                            size 40
                                            color "#ffffff"
                                            yalign 0.5
                                            default ""
                                            copypaste True

                                        if not addon_search_query:
                                            text "Поиск по названию, описанию или автору...":
                                                font "font/russia.ttf"
                                                size 40
                                                color "#666666"
                                                yalign 0.5
                            null height 10
                            
                            # Отображение количества найденных модов
                            if addon_search_query:
                                $ filtered_count = len(get_filtered_addons())
                                text "Найдено: [filtered_count]":
                                    font "font/russia.ttf"
                                    size 32
                                    color "#aaaaaa"
                                    xalign 0.0
                            
                            null height 5
                            
                            viewport id "addons_viewport":
                                draggable True
                                mousewheel True
                                scrollbars "vertical"
                                xsize 1060
                                ysize 690
                                
                                vbox:
                                    spacing 8
                                    
                                    $ filtered_addons = get_filtered_addons()
                                    
                                    if filtered_addons:
                                        for label, addon in filtered_addons:
                                            button:
                                                xsize 1020
                                                ysize 100
                                                background Solid("#ffffff11")
                                                hover_background Solid("#ffffff33")
                                                hover_sound None
                                                hovered [SetVariable("selected_addon", addon)]
                                                action [SetField(persistent, "jump_to", label), Start(label)]
                                                
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
                                                            text addon.get_authors_text():
                                                                size 28
                                                                color "#aaaaaa"
                                                                xmaximum 900
                                                                xalign 0.0
                                    else:
                                        vbox:
                                            xalign 0.5
                                            yalign 0.5
                                            spacing 20
                                            
                                            text "🔍" size 80 color "#333333" xalign 0.5
                                            
                                            text "Ничего не найдено":
                                                size 32
                                                color "#666666"
                                                xalign 0.5
                                            
                                            text "Попробуйте изменить поисковый запрос":
                                                size 20
                                                color "#555555"
                                                xalign 0.5

                    # инфа о моде
                    frame:
                        xsize 560
                        ysize 880
                        background Solid("#00000099")
                        padding (15, 15)
                        
                        if selected_addon:
                            vbox:
                                spacing 20
                                xfill True
                                
                                text "ИНФОРМАЦИЯ ОБ АДДОНЕ" size 48 color "#ffffff" font "font/russia.ttf" 
                                
                                null height 10
                                
                                if selected_addon.avatar:
                                    frame:
                                        xalign 0.5
                                        padding (10, 10)
                                        xmaximum 256
                                        ymaximum 256
                                        
                                        add selected_addon.avatar:
                                            fit "contain"
                                            xalign 0.5
                                            yalign 0.5
                                else:
                                    add "TBAddonManager/assets/images/avatar_placeholder.png" xsize 256 ysize 256 xalign 0.5
                                
                                null height 20
                                
                                text selected_addon.name:
                                    size selected_addon.get_adaptive_name_size()
                                    color "#ffffff" 
                                    font "font/russia.ttf" 
                                    xalign 0.5
                                    text_align 0.5
                                    xmaximum 500
                                
                                if selected_addon.authors:
                                    text selected_addon.get_full_authors_text():
                                        size 32
                                        color "#aaaaaa"
                                        xalign 0.5
                                        text_align 0.5
                                        xmaximum 500
                                
                                #null height 20
                                
                                python:
                                    import math
                                    desc_text = selected_addon.description
                                    chars_per_line = 50
                                    estimated_lines = math.ceil(len(desc_text) / chars_per_line)
                                    line_height = 24  # примерная высота строки
                                    estimated_height = estimated_lines * line_height
                                    needs_scrollbar = estimated_height > 220
                                
                                # Описание с условным скроллбаром
                                frame:
                                    xfill True
                                    background Solid("#ffffff11")
                                    padding (15, 15)
                                    xmaximum 500
                                    ymaximum 250
                                    
                                    if needs_scrollbar:
                                        viewport id "description_viewport":
                                            draggable True
                                            mousewheel True
                                            scrollbars "vertical"
                                            xsize 450
                                            ysize 220
                                            
                                            text selected_addon.description:
                                                size 18
                                                font "font/GenEiAntiqueNv5-M.ttf"
                                                color "#dddddd"
                                                text_align 0.0
                                                xalign 0.0
                                                xmaximum 440
                                    else:
                                        viewport id "description_viewport_no_scroll":
                                            xsize 470
                                            ysize 220
                                            
                                            text selected_addon.description:
                                                size 18
                                                font "font/GenEiAntiqueNv5-M.ttf"
                                                color "#dddddd"
                                                text_align 0.0
                                                xalign 0.0
                                                xmaximum 470
                                                
                        else:
                            # Заглушка, когда ничего не выбрано
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 30
                                
                                text "?" size 120 color "#333333" xalign 0.5
                                
                                text "Выберите мод из списка\nчтобы увидеть информацию":
                                    size 20
                                    color "#666666"
                                    text_align 0.5
                                    xalign 0.5
        else:
            frame:
                xalign 0.5
                yalign 0.4
                background Solid("#000000cc")
                padding (50, 50)
                
                vbox:
                    spacing 30
                    
                    text "МОДЫ НЕ НАЙДЕНЫ" size 40 color "#ffffff" bold True xalign 0.5
                    text "Установите моды в папку игры":
                        size 24
                        color "#aaaaaa"
                        xalign 0.5

        frame:
            xalign 0.5
            background Solid("#00000099")
            padding (5, 5)

            button:
                background Solid("#ffffff11")
                hover_background Solid("#ffffff33")
                padding (30, 20)
                xmaximum 150
                ymaximum 50
                action Return()

                text "Назад":
                    size 38
                    color "#ffffff"
