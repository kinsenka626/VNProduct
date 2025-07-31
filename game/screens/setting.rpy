# setting.rpy - 设置主界面 (只包含导航和背景)
image setting_background:
    "bg_setting.jpg"

screen setting():
    tag menu
    add "setting_background"
    # 左上角标题 (根据图片)
    fixed:
        pos (50, 50)
        text "chuanyue":
            size 36
            color "#FFDAB9"
            outlines [(2, "#FFEBCD", 0, 0)]
    
    # 选项卡导航栏 (左侧垂直排列)
    hbox:
        align(0.9, 0.035)
        spacing 40
        
        # 选项卡按钮 (红色字体匹配图片)
        textbutton _("显示"):
            action [SetScreenVariable("current_tab", "display"), Play("sound", "audio/sfx/click.wav")]
            style "selected_tab_button"  # 默认选中"显示"
        
        textbutton _("文字"):
            action [SetScreenVariable("current_tab", "text"), Play("sound", "audio/sfx/click.wav")]
            style "tab_button"
        
        textbutton _("确认"):
            action [SetScreenVariable("current_tab", "dialog"), Play("sound", "audio/sfx/click.wav")]
            style "tab_button"
        
        textbutton _("声音"):
            action [SetScreenVariable("current_tab", "sound"), Play("sound", "audio/sfx/click.wav")]
            style "tab_button"
        
        textbutton _("语音"):
            action [SetScreenVariable("current_tab", "voice"), Play("sound", "audio/sfx/click.wav")]
            style "tab_button"
        
        # 返回主菜单按钮
    textbutton _("返回"):
        align(0.9, 0.95)
        style "return_tab_button"
        action Return()
    
    # 默认选中的选项卡
    default current_tab = "display"
    
    # 右侧灰色面板 (包含所有设置内容)
    frame:
        background Solid("#CCCCCCCC")  # 灰色半透明面板
        pos (10, 100)
        xsize config.screen_width 
        ysize config.screen_height -100
        
        # 根据当前选项卡显示内容
        if current_tab == "display":
            use display_settings  # 包含显示设置子界面
        elif current_tab == "text":
            use text_settings
        elif current_tab == "dialog":
            use dialog_settings
        elif current_tab == "sound":
            use sound_settings
        elif current_tab == "voice":
            use voice_settings

# 选项卡按钮样式
style tab_button:
    background None
    padding (15, 10)
    font gui.interface_text_font
    size 26
    color "#FAF0E6"
    hover_color "#FF0000"  # 悬停时变红色
    outlines []

# 当前选中的选项卡样式
style selected_tab_button:
    background Solid("#E6E6FA", corner_radius=5)  # 红色背景匹配图片
    padding (15, 10)
    font gui.interface_text_font
    size 26
    color "#FF0000"  # 红色字体匹配图片
    hover_color "#FF0000"
    outlines []

# 返回按钮样式
style return_tab_button:
    background Solid("#F0F8FF", corner_radius=5)
    padding (15, 10)
    font gui.interface_text_font
    size 26
    color "#FFFFFF"
    hover_color "#FFD700"
    margin (0, 30, 0, 0)  # 上方留出间距