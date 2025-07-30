# 单独设置界面

screen setting():

    tag menu

    add HBox(Transform("#FFFFFF", ysize=70), "#000000")

    viewport:
        hbox:
            align (0.8, 0.0)
            spacing 30

            textbutton _("设置") action ShowMenu("preferences")
            textbutton _("设置") action ShowMenu("preferences")
            textbutton _("设置") action ShowMenu("preferences")
            textbutton _("设置") action ShowMenu("preferences")
            textbutton _("设置") action ShowMenu("preferences")
            # textbutton _("文字") action ShowMenu("text")
            # textbutton _("确认") action ShowMenu("dialog")
            # textbutton _("音量") action ShowMenu("sound")
            # textbutton _("语音") action ShowMenu("voice")

        textbutton _("返回"):
            style "return_button"
            action Return()


style setting_viewport:
    xsize config.screen_width-420
    ysize config.screen_height-200
    align (0.5, 0.5)

style setting_side:
    yfill True
    align (1.0, 0.5)

style setting_vscrollbar:
    unscrollable "hide"

style setting_label:
    padding (10, 10)
style setting_label_text:
    size 45
