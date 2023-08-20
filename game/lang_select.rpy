


label splashscreen:


    image bg_idioma = "gui/lang_select/bg_idioma.png"

    if persistent.lang_selected == None:
        scene bg_idioma with dissolve
        call screen idiomas

    show black with dissolve

    pause 0.5

    return

screen idiomas():
    text _("Select Your Language:") xpos 904 ypos 200 xalign 0.5
    text _("Seleccione Su Idioma:") xpos 388 ypos 200 xalign 0.5
    imagebutton:
        idle "gui/lang_select/esp_idle.png"
        hover "gui/lang_select/esp_hover.png"
        focus_mask True
        action Jump("enespanol")
    imagebutton:
        idle "gui/lang_select/eng_idle.png"
        hover "gui/lang_select/eng_hover.png"
        focus_mask True
        action Jump("eningles")


label eningles:
    $ renpy.change_language("English")
    $ persistent.lang_selected = True
    show black with dissolve
    jump splashscreen

label enespanol:
    $ renpy.change_language(None)
    $ persistent.lang_selected = True
    show black with dissolve
    jump splashscreen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
