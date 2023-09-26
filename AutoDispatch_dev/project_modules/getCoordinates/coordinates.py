# coordinates.py

# 初始的坐标字典
coordinates_dict = {
    "派发": [],
    "运往地": [],
    "销售用途": [],
    "确认销售用途": [],
    "确认派发": [],
}

# 更新坐标字典的函数
def update_coordinates(key_name, x, y):
    if key_name in coordinates_dict:
        coordinates_dict[key_name] = [x, y]
