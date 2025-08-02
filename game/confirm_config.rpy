define persistent.confirm_settings = {
    # 覆盖存档时确认（防止误操作覆盖进度）
    "overwrite_save": True,
    
    # 读取存档时确认（避免意外加载旧存档）
    "load_save": True,
    
    # 返回标题画面时确认（防止误触丢失当前进度）
    "return_to_title": True,
    
    # 快进时确认（避免跳过重要剧情）
    "toggle_skip": True,
    
    # 删除存档时确认（防止误删存档文件）
    "delete_save": True
}
# define persistent.confirm_settings = {
#     if persistent.window_opacity is None:
#         persistent.window_opacity = 0.8  # 默认透明度
# }
default preferences.afm={
    "after_click":True
}