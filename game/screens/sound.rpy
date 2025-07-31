# display.rpy - 显示设置子界面

# 显示设置内容
screen sound_settings():
    # 设置项容器
    vbox:
        pos (40, 40)
        spacing 35
        text '4'
        # # 显示模式设置 (图片中的第一个设置项)
        # vbox:
        #     # 标题使用红色字体
        #     text _("显示模式"):
        #         style "setting_label"
            
        #     hbox:
        #         spacing 40
        #         # 窗口按钮
        #         button:
        #             action [Preference("display", "window"), Play("sound", "audio/sfx/click.wav")]
        #             hovered Play("sound", "audio/sfx/hover.wav")
        #             background None
        #             has hbox
        #             # 使用红圈黑点表示选中状态
        #             add "gui/radio_selected.png" yalign 0.5  # 默认选中
        #             text _(" 窗口") style "setting_option"
                
        #         # 全屏按钮
        #         button:
        #             action [Preference("display", "fullscreen"), Play("sound", "audio/sfx/click.wav")]
        #             hovered Play("sound", "audio/sfx/hover.wav")
        #             background None
        #             has hbox
        #             add "gui/radio_unselected.png" yalign 0.5
        #             text _(" 全屏") style "setting_option"
        
        # # UI语言设置 (图片中的第二个设置项)
        # vbox:
        #     text _("UI"):
        #         style "setting_label"
            
        #     hbox:
        #         spacing 40
        #         # 简体字按钮
        #         button:
        #             action [SetField(persistent, "ui_language", "zh-simplified"), Play("sound", "audio/sfx/click.wav")]
        #             hovered Play("sound", "audio/sfx/hover.wav")
        #             background None
        #             has hbox
        #             # 使用红圈黑点表示选中状态
        #             add "gui/radio_selected.png" yalign 0.5  # 默认选中
        #             text _(" 简体字") style "setting_option"
                
        #         # 繁体字按钮
        #         button:
        #             action [SetField(persistent, "ui_language", "zh-traditional"), Play("sound", "audio/sfx/click.wav")]
        #             hovered Play("sound", "audio/sfx/hover.wav")
        #             background None
        #             has hbox
        #             add "gui/radio_unselected.png" yalign 0.5
        #             text _(" 繁体字") style "setting_option"
        
        # # 自动返回设置 (图片中的第三个设置项)
        # vbox:
        #     text _("保存后直接返回到游戏"):
        #         style "setting_label"
            
        #     hbox:
        #         spacing 40
        #         # 开启按钮
        #         button:
        #             action [SetField(persistent, "auto_return", True), Play("sound", "audio/sfx/click.wav")]
        #             hovered Play("sound", "audio/sfx/hover.wav")
        #             background None
        #             has hbox
        #             # 使用红圈黑点表示选中状态
        #             add "gui/radio_selected.png" yalign 0.5  # 默认选中
        #             text _(" 开启") style "setting_option"
                
        #         # 关闭按钮
        #         button:
        #             action [SetField(persistent, "auto_return", False), Play("sound", "audio/sfx/click.wav")]
        #             hovered Play("sound", "audio/sfx/hover.wav")
        #             background None
        #             has hbox
        #             add "gui/radio_unselected.png" yalign 0.5
        #             text _(" 关闭") style "setting_option"

# 设置项标签样式
style setting_label:
    size 28
    color "#FF0000"  # 红色字体匹配图片
    # font gui.sans_font
    bold True
    yalign 0.0
    outlines [(1, "#000000", 0, 0)]  # 黑色描边增强可读性

# 设置选项文本样式
style setting_option:
    size 24
    color "#000000"  # 黑色文字匹配图片
    font gui.interface_text_font