## Game Menu screen ############################################################
##
## 这列出了游戏菜单屏幕的基本通用结构。它被称为替换为屏幕标题，并显示标题和导航。
##
## 此屏幕不再包含背景，并且不再嵌入其内容。它旨在从任何给定菜单中轻松删除屏幕，因此您需要完成一些繁重的工作为菜单屏幕的内容设置容器。
##

screen save(title):

    style_prefix "save_menu"

    hbox:
        align (0, 0.0)
        spacing 30

        textbutton _("保存") action ShowMenu("save")

        textbutton _("加载") action ShowMenu("load")


    textbutton _("返回"):
        style "return_button"
        action Return()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style return_button:
    xpos 60
    yalign 1.0
    yoffset -45

style save_menu_viewport:
    xsize config.screen_width-420
    ysize config.screen_height-200
    align (0.5, 0.5)

style save_menu_side:
    yfill True
    align (1.0, 0.5)

style save_menu_vscrollbar:
    unscrollable "hide"

style save_menu_label:
    padding (10, 10)
style save_menu_label_text:
    size 45
