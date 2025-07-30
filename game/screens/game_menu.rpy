## Game Menu screen ############################################################
##
## 这列出了游戏菜单屏幕的基本通用结构。它被称为替换为屏幕标题，并显示标题和导航。
##
## 此屏幕不再包含背景，并且不再嵌入其内容。它旨在从任何给定菜单中轻松删除屏幕，因此您需要完成一些繁重的工作为菜单屏幕的内容设置容器。
##

screen game_menu(title):

    style_prefix "game_menu"

    hbox:
        align (0, 0.0)
        spacing 30

        # textbutton _("历史") action ShowMenu("history")

        # textbutton _("保存") action ShowMenu("save")

        # textbutton _("加载") action ShowMenu("load")

        # textbutton _("设置") action ShowMenu("preferences")

        # if _in_replay:

        #     textbutton _("End Replay") action EndReplay(confirm=True)

        # elif not main_menu:

        #     textbutton _("标题界面") action MainMenu()

        # textbutton _("关于") action ShowMenu("about")

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        #     ## Help isn't necessary or relevant to mobile devices.
        #     textbutton _("帮助") action ShowMenu("help")

        # if renpy.variant("pc"):

        #     ## The quit button is banned on iOS and
        #     ## unnecessary on Android and Web.
        #     textbutton _("退出") action Quit(confirm=not main_menu)

    textbutton _("返回"):
        style "return_button"
        action Return()

    ## Remove this line if you don't want to show the screen
    ## title text as a label (for example, if it's baked into
    ## the background image.)
    # label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style return_button:
    xpos 60
    yalign 1.0
    yoffset -45

style game_menu_viewport:
    xsize config.screen_width-420
    ysize config.screen_height-200
    align (0.5, 0.5)

style game_menu_side:
    yfill True
    align (1.0, 0.5)

style game_menu_vscrollbar:
    unscrollable "hide"

style game_menu_label:
    padding (10, 10)
style game_menu_label_text:
    size 45
