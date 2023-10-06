# 自动化模拟鼠标事件
import pyautogui
# 获取键盘事件
from pynput import keyboard

from project_modules.auto_click.auto_click import start_auto_click
from project_modules.initial_data.initial_data import (
    update_anchor_point,
)

# 创建键盘监听器
keyboard_listener = None


def on_key_press(key):
    x, y = pyautogui.position()

    try:
        key_name = key.char
        print("coordinate: ", x, y)
    except AttributeError:
        key_name = str(key)
        print(key_name)

    if key_name == 'r':
        update_anchor_point(x, y)
        return False
        # print("已获取到小程序定位，请按下【回车】继续，如需退出请按【ESC】")
    # elif key_name == 'Key.enter':
    #     return False    # 停止监听器


def start_keyboard_listener():
    global keyboard_listener

    # 创建键盘监听器
    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    # 启动监听器
    print("正在获取定位坐标...\n请将鼠标放置在小程序左上角并按下\'r\'键获取坐标")
    keyboard_listener.start()

    keyboard_listener.join()

    # 停止监听器
    keyboard_listener.stop()
