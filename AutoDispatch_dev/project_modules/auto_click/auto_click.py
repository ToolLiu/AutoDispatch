import pyautogui
import time

from project_modules.get_coordinates.coordinates import coordinates_dict, anchor_point
from project_modules.auto_click.call_api import get_orders
from .r_input import r_input

orders = get_orders()
def start_auto_click():
    for order in orders:
        print("正在派单---",order["u_license_plate"],"---",order["u_name"])
    # 点击坐标的顺序列表
    # click_order = ['派发', '运往地', '销售用途', '确认销售用途', '确认派发']

    # 如果coordinates_dict字典没存满则退出执行程序
    # for item in coordinates_dict.values():
    #     if len(item) == 0:
    #         print("坐标字典：", coordinates_dict, "\n请检查输入是否有误或有漏输。")
    #         return 0
    if anchor_point["x"] == None:
        print("未找到定位坐标，请重新运行小程序并定位")

    # for order in orders:
    #     print(order)
    click_event(303, 275, 0.5)
    click_event(210, 122, 1.5)
    r_input("sms")
    click_event(108, 109, 0.2)
    click_event(315, 187, 0.2)

    # 遍历点击顺序列表，按顺序自动点击坐标
    # for item in click_order:
        # x, y = coordinates_dict[item]
        # if item == '派发':
        #     click_event(x, y, 0.5)
        # elif item == '运往地':
        #     click_event(x, y, 1.5)
        # elif item == '销售用途':
        #     r_input("sms")
        #     time.sleep(0.5)
        #     click_event(x, y, 0.2)
        # elif item == '确认销售用途':
        #     click_event(x, y, 0.3)
        # elif item == '确认派发':
        #     click_event(x, y, 0.5)

def click_event(x, y, waitTime):
    pyautogui.click(anchor_point["x"] + x, anchor_point["y"] + y)  # 模拟点击事件
    time.sleep(waitTime)  # 等待time秒
