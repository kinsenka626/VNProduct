
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like
image main_menu_background:
    "bg_1.png"

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_background"


    vbox:
        xpos 160
        yalign 0.5
        spacing 30
        if renpy.newest_slot(regexp=None):
            # 如果玩家有存档则加载最新的存档，Continue()为renpy默认函数
            textbutton _("继续游戏") action Continue()

        textbutton _("开始游戏") action Start()

        textbutton _("加载游戏") action ShowMenu("load")

        textbutton _("游戏设置") action ShowMenu("setting")

        textbutton _("关于") action ShowMenu("about")

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        #     ## Help isn't necessary or relevant to mobile devices.
        #     textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("退出游戏") action Quit(confirm=not main_menu)

