# coordinates.py

# 初始的坐标字典
coordinates_dict = {
    "派发": [],
    "运往地": [],
    "运往地_确认": [],
    "销售用途": [],
    "销售用途_确认": [],
    "车号": [],
    "确认派发": [],
}

anchor_point = {"x": None, "y": None}

# 更新坐标字典的函数
def update_coordinates(key_name, x, y):
    if key_name in coordinates_dict:
        coordinates_dict[key_name] = [x, y]

def update_anchor_point(x, y):
    anchor_point["x"] = x
    anchor_point["y"] = y
