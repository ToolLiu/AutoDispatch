import pyautogui
import time

from pynput import keyboard
from project_modules.initial_data.initial_data import anchor_point
from project_modules.auto_click.call_api import get_orders, updateCoalBillNum
from .r_input import r_input

orders = get_orders()
coal_bill_number = None
# 全局变量，用于表示是否要退出循环
exit_loop = False
# 全局变量，用于判断是否跳过本次循环
skip_loop = False
skip_num = 0


def on_press(key):
    global skip_loop
    global skip_num
    global exit_loop
    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key)

    if key_name == 'Key.enter':
        return False
    elif key_name == 'n':
        skip_loop = True
        skip_num = skip_num + 1
        return False
    elif key_name == 'Key.esc':
        exit_loop = True
        return False
    print(key)


def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        print("信息正确请按【回车】键，跳过本单请按【n】，退出请按【ESC】")
        listener.join()


def start_auto_click():
    global skip_loop
    global coal_bill_number
    coal_bill_number = int(input("请输入初始提煤单号：ELTE"))
    print("ELTE" + str(coal_bill_number))

    if anchor_point["x"] is None:
        print("未找到定位坐标，请重新运行小程序并定位")

    for index, order in enumerate(orders):
        print("正在派单---", order["u_license_plate"], "---", order["u_name"])
        # 派单
        click_event(303, 275, 0.5)
        # 运往地
        click_event(210, 122, 1.5)
        # 输入运往地
        r_input("sms")
        time.sleep(0.1)
        # 点击输入后的搜索内容
        click_event(108, 109, 0.2)
        # 销售用途
        click_event(315, 187, 0.2)
        # 煤场用煤
        click_event(385, 508, 0.3)
        # 车号
        click_event(190, 347, 0.5)
        # 输入车号
        r_input(order["u_license_plate"])
        time.sleep(0.6)
        # 选择车号
        click_event(108, 109, 0.2)
        bill_num = "ELTE" + str(coal_bill_number + index - skip_num)
        print("请核对提煤单号和页面上的司机姓名：", bill_num, order["u_name"])
        start_keyboard_listener()
        if exit_loop:
            break  # 如果退出标志为 True，则退出循环
        elif skip_loop:
            skip_loop = False
            continue    # 如果skip_loop为 True，则进入下一次循环
        else:
            print(666)
            # updateCoalBillNum(order["coal_order_id"], bill_num)
            # click_event(206, 734, 0.5)


def click_event(x, y, waitTime):
    pyautogui.click(anchor_point["x"] + x, anchor_point["y"] + y)  # 模拟点击事件
    time.sleep(waitTime)  # 等待time秒
