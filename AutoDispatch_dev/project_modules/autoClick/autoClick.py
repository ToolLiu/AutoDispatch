import pyautogui
import time

from ..getCoordinates.coordinates import coordinates_dict

def start_auto_click():
    # 点击坐标的顺序列表
    click_order = ['订单', '抢单', '搜索', '查询']

    # 遍历点击顺序列表，按顺序自动点击坐标
    for item in click_order:
        if item in coordinates_dict:
            x, y = coordinates_dict[item]
            pyautogui.click(x, y)  # 模拟点击事件
            time.sleep(1)  # 等待1秒