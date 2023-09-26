import pyautogui
import time

from ..getCoordinates.coordinates import coordinates_dict

def start_auto_click():
    # 点击坐标的顺序列表
    click_order = ['派发', '运往地', '销售用途', '确认销售用途', '确认派发']

    # 遍历点击顺序列表，按顺序自动点击坐标
    for item in click_order:
        x, y = coordinates_dict[item]
        if item == '派发':
            click_event(x, y, 0.5)
        elif item == '运往地':
            click_event(x, y, 0.5)
        elif item == '销售用途':
            click_event(x, y, 0.2)
        elif item == '确认销售用途':
            click_event(x, y, 0.2)
        elif item == '确认派发':
            click_event(x, y, 0.5)

def click_event(x, y, waitTime):
    pyautogui.click(x, y)  # 模拟点击事件
    time.sleep(waitTime)  # 等待time秒
