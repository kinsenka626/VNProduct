# display.rpy - 显示设置子界面（已匹配UI设计）
image idle_screen_button:
    "Elements/Menu/button.png"
    zoom 0.5  #
image hover_screen_button:
    "Elements/Menu/button_hover.png"
    zoom 0.5  # 白底灰框
# 显示设置内容
screen display_settings():
    # 设置项容器
    vbox:
        align(0.5, 0.15)
        box_align 1
        spacing 60
        hbox:
            first_spacing 200
            # xminimum 150
            # yminimum 40
            box_align 0.5
            spacing 100
            # xalign 0.5
            frame:
                minimum (400,64)
                maximum (400,64)
                text _("屏幕显示模式："):
                    size 28
                    color "#DB7093"
                    xalign 0
                    yalign 0.5
            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    yalign 1
                    xalign 1
                    action [Preference("display", "window"), Play("sound", "audio/sfx/click.wav")]
                    hovered Play("sound", "audio/sfx/hover.wav")
                    idle_background "idle_screen_button"
                    hover_background "hover_screen_button"
                    selected_idle_background "hover_screen_button"
                text _("Window"):
                    color "#DB7093"  
                    size 24
                    xalign 0.5
                    yalign 0.5
            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    action [Preference("display", "fullscreen"), Play("sound", "audio/sfx/click.wav")]
                    hovered Play("sound", "audio/sfx/hover.wav")
                    idle_background "idle_screen_button"
                    hover_background "hover_screen_button"
                    selected_idle_background "hover_screen_button"             
                text _("Fullscreen"):
                    color "#DB7093"  
                    size 24
                    xalign 0.5
                    yalign 0.5
        hbox:
            first_spacing 200
            box_align 0.5
            spacing 100
            frame:
                minimum (400,64)
                maximum (400,64)
                text _("覆盖存档时进行确认："):
                    size 28
                    color "#DB7093"
                    xalign 0
                    yalign 0.5
            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    selected (persistent.confirm_settings["overwrite_save"] == True)
                    action [
                    SetDict(persistent.confirm_settings, "overwrite_save", True),
                    Play("sound", "audio/sfx/click.wav")  # 添加点击音效
                    ]
                    hovered Play("sound", "audio/sfx/hover.wav")
                    idle_background "idle_screen_button"
                    hover_background "hover_screen_button"
                    selected_idle_background "hover_screen_button"
                text _("开启"):
                    color "#DB7093" 
                    hover_color "#FFFFFF"
                    size 24
                    align (0.5,0.5)

            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    selected (persistent.confirm_settings["overwrite_save"] == False)
                    action [
                    SetDict(persistent.confirm_settings, "overwrite_save", False),
                    Play("sound", "audio/sfx/click.wav")  # 添加点击音效
                    ]
                    hovered Play("sound", "audio/sfx/hover.wav")
                    idle_background "idle_screen_button"
                    hover_background "hover_screen_button"  
                    selected_idle_background "hover_screen_button"          
                text _("关闭"):
                    color "#DB7093"  
                    size 24
                    xalign 0.5
                    yalign 0.5  
        hbox:
            first_spacing 200
            box_align 0.5
            spacing 100
            frame:
                minimum (400,64)
                maximum (400,64)
                text _("读取存档时确认："):
                    size 28
                    color "#DB7093"
                    xalign 0
                    yalign 0.5
            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    selected (persistent.confirm_settings["load_save"] == True)
                    action [
                    SetDict(persistent.confirm_settings, "load_save", True),
                    Play("sound", "audio/sfx/click.wav")  # 添加点击音效
                    ]
                    hovered Play("sound", "audio/sfx/hover.wav")
                    idle_background "idle_screen_button"
                    hover_background "hover_screen_button"
                    selected_idle_background "hover_screen_button"
                text _("开启"):
                    color "#DB7093" 
                    hover_color "#FFFFFF"
                    size 24
                    align (0.5,0.5)

            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    selected (persistent.confirm_settings["load_save"] == False)
                    action [
                    SetDict(persistent.confirm_settings, "load_save", False),
                    Play("sound", "audio/sfx/click.wav")  # 添加点击音效
                    ]
                    hovered Play("sound", "audio/sfx/hover.wav")
                    idle_background "idle_screen_button"
                    hover_background "hover_screen_button"  
                    selected_idle_background "hover_screen_button"          
                text _("关闭"):
                    color "#DB7093"  
                    size 24
                    xalign 0.5
                    yalign 0.5 
        hbox:
            first_spacing 200
            box_align 0.5
            spacing 100
            frame:
                minimum (400,64)
                maximum (400,64)
                text _("删除存档时确认："):
                    size 28
                    color "#DB7093"
                    xalign 0
                    yalign 0.5
            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    selected (persistent.confirm_settings["delete_save"] == True)
                    action [
                    SetDict(persistent.confirm_settings, "delete_save", True),
                    Play("sound", "audio/sfx/click.wav")  # 添加点击音效
                    ]
                    hovered Play("sound", "audio/sfx/hover.wav")
                    idle_background "idle_screen_button"
                    hover_background "hover_screen_button"
                    selected_idle_background "hover_screen_button"
                text _("开启"):
                    color "#DB7093" 
                    hover_color "#FFFFFF"
                    size 24
                    align (0.5,0.5)

            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    selected (persistent.confirm_settings["delete_save"] == False)
                    action [
                    SetDict(persistent.confirm_settings, "delete_save", False),
                    Play("sound", "audio/sfx/click.wav")  # 添加点击音效
                    ]
                    hovered Play("sound", "audio/sfx/hover.wav")
                    idle_background "idle_screen_button"
                    hover_background "hover_screen_button"  
                    selected_idle_background "hover_screen_button"          
                text _("关闭"):
                    color "#DB7093"  
                    size 24
                    xalign 0.5
                    yalign 0.5 
        hbox:
            first_spacing 200
            box_align 0.5
            spacing 100
            frame:
                minimum (400,64)
                maximum (400,64)
                text _("返回标题画面时确认："):
                    size 28
                    color "#DB7093"
                    xalign 0
                    yalign 0.5
            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    selected (persistent.confirm_settings["return_to_title"] == True)
                    action [
                    SetDict(persistent.confirm_settings, "return_to_title", True),
                    Play("sound", "audio/sfx/click.wav")  # 添加点击音效
                    ]
                    hovered Play("sound", "audio/sfx/hover.wav")
                    idle_background "idle_screen_button"
                    hover_background "hover_screen_button"
                    selected_idle_background "hover_screen_button"
                text _("开启"):
                    color "#DB7093" 
                    hover_color "#FFFFFF"
                    size 24
                    align (0.5,0.5)

            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    selected (persistent.confirm_settings["return_to_title"] == False)
                    action [
                    SetDict(persistent.confirm_settings, "return_to_title", False),
                    Play("sound", "audio/sfx/click.wav")  # 添加点击音效
                    ]
                    hovered Play("sound", "audio/sfx/hover.wav")
                    idle_background "idle_screen_button"
                    hover_background "hover_screen_button"  
                    selected_idle_background "hover_screen_button"          
                text _("关闭"):
                    color "#DB7093"  
                    size 24
                    xalign 0.5
                    yalign 0.5


# 设置项标签样式
style setting_label:
    size 28
    color "#000000"
    bold True
    yalign 0.0
