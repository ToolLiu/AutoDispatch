import pyautogui
import time

from ..getCoordinates.coordinates import coordinates_dict

def start_auto_click():
    # 点击坐标的顺序列表
    click_order = ['派发', '运往地', '销售用途', '确认销售用途', '确认派发']

    # 如果coordinates_dict字典没存满则退出执行程序
    for item in coordinates_dict.values():
        if len(item) == 0:
            print("坐标字典：", coordinates_dict, "\n请检查输入是否有误或有漏输。")
            return 0

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
            click_event(x, y, 0.3)
        elif item == '确认派发':
            click_event(x, y, 0.5)

def click_event(x, y, waitTime):
    pyautogui.click(x, y)  # 模拟点击事件
    time.sleep(waitTime)  # 等待time秒
