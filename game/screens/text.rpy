# text.rpy - 显示设置子界面
image empty_bar:
    "gui/bar/bar_empty.png"
image filled_bar:
    "gui/bar/bar_filled.png"
# 显示设置内容
screen text_settings():
    # 设置项容器
    vbox:
        align(0.5, 0.15)
        spacing 60
        vbox:

            spacing 30
            
            # 标题区域
            hbox:
                xfill True
                yalign 0.0
                label "文字持续播放演示" style "demo_title"
            
            # 文字演示区域
            frame:
                style "demo_text_frame"
                xfill True
                ysize 180
                
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
                label "播放速度" style "demo_label" xsize 200
                bar:
                    value ScreenVariable("demo_speed")
                    range (0.1, 10.0) # 速度范围：0.1秒/字 - 10秒/字
                    step 0.1
                    style "demo_slider"
                    xmaximum 400
            
            # 显示当前速度值
            text "当前速度: [demo_speed:.1f] 秒/字" style "demo_speed_text"

# 样式定义
init python:
    # 计算当前时间的函数
    import time
    def get_current_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 屏幕变量定义
default demo_playing = False
default demo_speed = 0.5 # 默认速度（秒/字）
default demo_text = "KANADE > 请选择示例文本开始播放演示"

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
    background Solid("#f0f8ff") # 浅蓝色背景
    padding (20, 15)
    ysize 180

style demo_label:
    color "#2e8b57"
    size 24
    bold True

style demo_slider:
    left_bar "gui/slider_full.png" # 绿色滑块
    right_bar "gui/slider_empty.png"
    thumb "gui/slider_thumb.png"
    thumb_offset 12

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