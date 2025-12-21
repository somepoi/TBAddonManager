screen addons:
    modal True tag menu
    style_prefix "main_menu"


    vbox at mm_elements:
        xalign 0.47
        yalign 0.4

        for lbl, name in sorted(addons.iteritems()):
            textbutton name:
                action (Start(lbl))
                if preferences.language == "japan":
                    text_font other_font_interface
                keyboard_focus False

        textbutton "Назад":
            action Return()
            if preferences.language == "japan":
                text_font other_font_interface
            keyboard_focus False

    vbox:
        xalign 0.47
        yalign 0.4

        for lbl, name in sorted(addons.iteritems()):
            button:
                background "interface/main_meny/plaska.png"
                text name:
                    if preferences.language == "japan":
                        font other_font_interface
                at mm_but
                action (Start(lbl))
                default_focus True
        button:
            background "interface/main_meny/plaska.png"
            text _("Назад"):
                if preferences.language == "japan":
                    font other_font_interface
            at mm_but
            action Return()
    # window:
    #     if addons:
    #         side "c b r":
    #             area (0.27, 0.24, 0.47, 0.70)
    #             viewport id "addons":
    #                 draggable True
    #                 mousewheel True
    #                 scrollbars None
    #                 yinitial 0.0

    #                 has grid 1 len(addons)
    #                 for lbl, name in sorted(addons.iteritems()):
    #                     textbutton name action (SetField(persistent, "jump_to", lbl), Start())

    #         bar value XScrollValue("addons")
    #         vbar value YScrollValue("addons")
