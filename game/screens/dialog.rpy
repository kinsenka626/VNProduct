# display_screen.rpy - 显示设置界面

screen display():
    # 屏幕标签定义
    tag menu
    
    # 固定当前标签变量
    default current_tab = "display"
    
    # 背景设置
    add "#FFDEAD"  # 白色背景
    
    # 标题区域
    fixed:
        pos (50, 50)
        text "TEMP":
            size 48
            color "#000000"
            outlines []  # 移除文字描边
        text "DISPLAY":  # 修改为当前页面的标题
            pos (0, 70)
            size 36
            color "#000000"
            outlines []  # 移除文字描边
    
    # 选项卡导航
    hbox:
        align (0.5, 0.15)
        spacing 30
        
        # 当前选项卡高亮显示
        textbutton _("DISPLAY"):
            action NullAction()  # 禁用点击
            style "tab_button"
            selected_idle_foreground "#FFD700"
            selected_hover_foreground "#FFD700"
        
        # 其他选项卡可以点击
        textbutton _("TEXT"):
            action ShowMenu("text")
            style "tab_button"
        
        textbutton _("DIALOG"):
            action ShowMenu("dialog")
            style "tab_button"
        
        textbutton _("SOUND"):
            action ShowMenu("sound")
            style "tab_button"
        
        textbutton _("VOICE"):
            action ShowMenu("voice")
            style "tab_button"
    
    # 设置内容区域
    frame:
        style_prefix ""
        background Solid("#FFFFFF")
        xsize config.screen_width - 100
        ysize config.screen_height - 250
        align (0.5, 0.5)
        top_padding 50
        bottom_padding 50
        
        # 显示模式设置
        vbox:
            spacing 20
            
            # 显示模式
            hbox:
                xfill True
                text _("显示模式") style "pref_label"
                null width 100
                textbutton _("窗口"):
                    style "radio_button"
                    selected not preferences.fullscreen
                    action Preference("display", "window")
                null width 20
                textbutton _("全屏"):
                    style "radio_button"
                    selected preferences.fullscreen
                    action Preference("display", "fullscreen")
            
            # UI语言设置
            hbox:
                xfill True
                text _("UI") style "pref_label"
                null width 100
                textbutton _("简体字"):
                    style "radio_button"
                    selected True  # 这里应替换为真实的语言状态
                    action NullAction()  # 替换为真实的语言设置动作
                null width 20
                textbutton _("繁体字"):
                    style "radio_button"
                    action NullAction()  # 替换为真实的语言设置动作
            
            # 保存后自动返回设置
            hbox:
                xfill True
                text _("保存后直接返回到游戏") style "pref_label"
                null width 100
                textbutton _("开启"):
                    style "radio_button"
                    action NullAction()  # 替换为真实的设置动作
                null width 20
                textbutton _("关闭"):
                    style "radio_button"
                    action NullAction()  # 替换为真实的设置动作
    
    # 底部按钮
    hbox:
        align (0.5, 0.95)
        spacing 50
        
        # textbutton _("设置") action Return()
        textbutton _("返回") action Return()

# 在同一个文件中定义所需的样式
style tab_button:
    background None
    hover_background Solid("#F0F0F0")
    padding (15, 8)
    font gui.interface_text_font
    size 24
    color "#000000"
    hover_color "#555555"
    outlines []

style radio_button:
    background None
    hover_background Solid("#F0F0F0")
    padding (10, 5)
    min_width 100
    color "#000000"
    hover_color "#555555"
    selected_color "#FFD700"  # 选中时为金色

style pref_label:
    size 22
    color "#000000"
    min_width 200
    xalign 0.0