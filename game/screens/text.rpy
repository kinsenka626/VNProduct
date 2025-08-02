# text.rpy - 显示设置子界面

image seek:
    "gui/bar/seek.png"
# 显示设置内容
screen text_settings():
    # 设置项容器
    vbox:
        align(0.5, 0.15)
        spacing 60
        minimum (1200,100)
        maximum (1200,300)
        vbox:
            align(0.5, 0.0)
            spacing 30
            
            # 标题区域
            # hbox:
            #     xfill True
            #     yalign 0.0
            #     label "文字持续播放演示" style "demo_title"
            
            # 文字演示区域
            frame:
                padding(10,10)
                style "demo_text_frame"
                xfill True
                ysize 100
                xsize 800
                vbox:
                    id "text_area"
                    if demo_playing:
                        text demo_text:
                            slow True # 启用逐字显示
                            # slow_speed preferences.text_cps # 控制显示速度
                            size 24
                            color "#333"
                    else:
                        text demo_text size 24 color "#333"
            # 速度控制滑块
        vbox:
            spacing 15
            xalign 0.5
            hbox:
                yalign 0.5
                label "播放速度" style "demo_label" xsize 200
                bar:
                    value Preference("text speed")
                    style "demo_bar"
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
                text _("点击继续播放："):
                    size 28
                    color "#DB7093"
                    xalign 0
                    yalign 0.5
            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    action [
                        Preference("auto-forward after click", "enable"),
                        Play("sound", "audio/sfx/click.wav")]
                    hovered Play("sound", "audio/sfx/hover.wav")
                    idle_background "idle_screen_button"
                    hover_background "hover_screen_button"
                    selected_idle_background "hover_screen_button"
                text _("开启"):
                    color "#DB7093"  
                    size 24
                    xalign 0.5
                    yalign 0.5
            frame:
                minimum (178,64)
                maximum (178,64)
                button:
                    action [Preference("auto-forward after click", "disable"), 
                    Play("sound", "audio/sfx/click.wav")]
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
                text _("快进方式："):
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




# 样式定义
init python:
    # 计算当前时间的函数
    import time
    def get_current_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 屏幕变量定义
default demo_playing = False
default demo_speed = 0.5 # 默认速度（秒/字）
default demo_text = "文字显示速度\nKANADE >>>>>>>>>>>>>>"
# default preferences.afm_after_click = True

# 样式
style demo_frame:
    background Frame("gui/frame_bg.png", 25, 25) # 带圆角的白色背景
    padding (40, 30)

style demo_title:
    color "#2e8b57" # 海绿色标题
    size 36
    xalign 0.5
    bold True

style demo_text_frame:
    background Solid("#F5F5F5") # 浅蓝色背景
    padding (0, 0)
    ysize 180

# 在 screens.rpy 或其他界面定义文件中添加
style demo_bar:
    # ysize 38  # 滑块轨道高度（基于第1张图的垂直空间）
    # 左侧填充条样式（基于第1张图的粉红色填充区）
    left_bar Frame(
        "gui/bar/bar_filled.png",  # 粉红色填充图片
        left=12, top=12, right=12, bottom=12,  # 圆角设置
        tile=False
    )
    # 右侧背景条样式（基于第1图的灰色背景）
    right_bar Frame(
        "gui/bar/bar_empty.png",  # 浅灰色背景图片
        left=12, top=12, right=12, bottom=12,  # 圆角设置
        tile=False
    )
    # 滑块控制柄样式（基于第2张图的"粉色长条中间有白色竖线"）
    thumb Transform(
        "gui/bar/seek.png",  # I形滑块图片
        zoom=1,
        fit="contain",  # 保持原始高宽比
        yalign=0.5  # 垂直居中
    )
    # 滑块位置偏移调整
    thumb_offset  -10  # 滑块宽度的一半，确保滑块在轨道上精确居中
    # 防止滑块超出轨道
    # 鼠标悬停时放大滑块，增强交互感
    hover_thumb Transform(
        "gui/bar/seek.png",
        fit="contain",
        zoom=1,  # 悬停放大20%
        yalign=0.5
    )


style demo_button:
    background "gui/button_idle.png"
    hover_background "gui/button_hover.png"
    padding (15, 8)
    min_width 150

style demo_speed_text:
    color "#555"
    size 20
    xalign 0.5


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