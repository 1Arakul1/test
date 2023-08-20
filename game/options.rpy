














define config.name = _("NarutoTrainer")





define gui.show_name = False

define gui.show_version = True




define config.version = "0.5"





define gui.about = _p("""
{b}Game Developer:{/b}\n
Luchetty

{a=https://www.patreon.com/Luchetty}Patreon{/a} - {a=https://luchetty.itch.io/realm-of-lust}Itch.io{/a} - {a=https://discord.com/invite/hDZYBg9A}Discord{/a}

{b}Music:{/b}\n
https://www.purple-planet.com/
""")



define build.name = "NarutoTrainer"








define config.has_sound = True
define config.has_music = True
define config.has_voice = True













define config.main_menu_music = "audio/bgm/Organ Donor.mp3"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)








default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "NarutoTrainer-1648069472"






define config.window_icon = "gui/window_icon.png"







init python:






















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
