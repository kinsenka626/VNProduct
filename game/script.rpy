# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define s = Character("Alice",image="character_Alice" ,  who_suffix="-兔女郎版本")
define l = Character("Emilia",image="character_Emilia", who_prefix="穿越的")
default loop_num = 3
image bg_old:
    "images/bg_old.jpg"
    zoom 1.1
image bg_2:
    "images/bg_2.png"
    zoom 1.0

image bg_moli="bg_moli.jpg"
image character_Emilia normal:
    "Emilia.png"
    zoom 0.2
    xalign 0.1  # 使用相对位置替代绝对位置
    yalign 1.0  # 底部对齐
image character_Alice normal:
    "Alice.png"
    zoom 0.15
    xalign 0.9  # 使用相对位置替代绝对位置
    yalign 1.0  # 底部对齐  
image side character_Alice:
    "Alice_icon.png"
    zoom 0.15
image side character_Emilia:
    "Emilia_icon.png"
    zoom 0.15









# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    show bg_2

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    show character_Emilia normal with dissolve
    show character_Alice normal with dissolve


    play music "autio/bgm_red.ogg" 
    

    # 此处显示各行对话。
    """
    爱丽丝走出了前哨基地
    基地外突然出现一整炫光
    """

    s "发生了什么"
    l "这里\n是哪"
    s "是{color=#ff0000}{rb}前哨基地{/rb}{rt}NIKKE的家园{/rt}{/color}{w=1.0}"


label meeting:
    show character_Emilia normal
    stop music
    menu optional_name:
        "你的选择"
        "打招呼":
            s "你是从哪里来的"
            $ loop_num=loop_num+1
            $ l = Character("Emilia", color="#f08989",who_prefix="警惕的",window_left_padding=160)
            l "我来自异世界"
        "默默走开":
            $ loop_num=loop_num-1
            s "与我无瓜"
    if loop_num>3:
        window hide dissolve
        pause
        s "很高兴认识你"
label end:
    return

