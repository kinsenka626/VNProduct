
## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## If there's a side image, display it in front of the text.
    add SideImage() xalign 0.1 yalign 1.0 yoffset -120 xoffset 140 


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

# Style for the dialogue window
style window:
    xalign 0.5
    yalign 1.0
    xysize (1031, 277)
    padding (40, 10, 40, 40)
    background Image("gui/textbox.png", xalign=0.8, yalign=1.0)

# Style for the dialogue
style say_dialogue:
    adjust_spacing False
    ypos 60

# The style for dialogue said by the narrator
style say_thought:
    is say_dialogue

# Style for the box containing the speaker's name
style namebox:
    xpos 20
    xysize (None, None)
    background Frame("gui/namebox.png", 5, 5, 5, 5, tile=False, xalign=0.0)
    padding (5, 5, 5, 5)

# Style for the text with the speaker's name
style say_label:
    color '#f93c3e'
    xalign 0.0
    yalign 0.5
    size gui.name_text_size
    font gui.name_text_font


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100
    

    if quick_menu:
                # Main container that handles hover effect
        fixed:
            align (0.0, 0.5)
            # Invisible trigger area (right edge of screen)
            mousearea:
                area (1720, 0, 200, 1.0) 
                hovered [Show("quick_menu_visible")]
                unhovered [Hide("quick_menu_visible")]
            
            # Visible sidebar (hidden by default)
            use quick_menu_visible

screen quick_menu_visible():
    # Actual visible menu content
    frame:
        align (1.0, 0.5)
        background None  # Transparent background
        padding (0, 0)
        margin (0, 0)
        
        at transform:
            alpha 0.0  # Start invisible
            on show:
                linear 0.2 alpha 1.0  # Fade in
            on hide:
                linear 0.2 alpha 0.0  # Fade out
        
        vbox:
            spacing 30
            style_prefix "quick"
            textbutton _("保存") action ShowMenu('save')
            textbutton _("加载") action ShowMenu("load")
            textbutton _("上文") action Rollback()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("跳过") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("设置") action ShowMenu('setting')
            # if persistent.confirm_settings["return_to_title"]
            #     textbutton _("标题") action MainMenu() 
            # else  
            #     textbutton _("标题") action MainMenu(confirm=False)
            # 在屏幕定义（如 screens.rpy 的 navigation 部分）
            textbutton _("标题"):
                action If(
                    persistent.confirm_settings.get("return_to_title", True),
                    MainMenu(confirm=True),   # 开启弹窗确认
                    MainMenu(confirm=False)   # 关闭弹窗，直接返回标题
                )
            textbutton _("帮助") action ShowMenu("help")
            textbutton _("退出") action Quit(confirm=not main_menu)




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_vbox:
    xalign 1.0
    yalign 0.5 
    spacing 8

style quick_button:
    background None
    padding (15, 6, 15, 0)
    # at transform:
    #     on hover:
    #         linear 0.1 xoffset 5  
    #     on idle:
    #         linear 0.1 xoffset 0  

style quick_button_text:
    size 21
    selected_color '#f93c3e'
    idle_color "#aaa"

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing 15

        use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

# The style for the NVL "textbox"
style nvl_window:
    is default
    xfill True yfill True
    background "gui/nvl.png"
    padding (0, 15, 0, 30)

# The style for the text of the speaker's name
style nvl_label:
    is say_label
    xpos 645 xanchor 1.0
    ypos 0 yanchor 0.0
    xsize 225
    min_width 225
    textalign 1.0

# The style for dialogue in NVL
style nvl_dialogue:
    is say_dialogue
    xpos 675
    ypos 12
    xsize 885
    min_width 885

# The style for dialogue said by the narrator in NVL
style nvl_thought:
    is nvl_dialogue

style nvl_button:
    xpos 675
    xanchor 0.0


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window:
    is empty
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    is empty
    xalign 0.5

style bubble_who:
    is default
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    is default
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}