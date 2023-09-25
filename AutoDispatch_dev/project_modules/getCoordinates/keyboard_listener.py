# 自动化模拟鼠标事件
import pyautogui
# 获取键盘事件
from pynput import keyboard

from project_modules.getCoordinates.coordinates import *

# 创建键盘监听器
keyboard_listener = None

def on_key_press(key):

    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key)
        print(key_name)

    if key_name == 'r':
        x, y = pyautogui.position()
        print(f"Mouse position({key_name}): x={x}, y={y}")
        update_coordinates("first", x, y)
    elif key_name == 'Key.esc':
        keyboard_listener.stop()  # 停止监听器

def start_keyboard_listener():
    global keyboard_listener

    # 创建键盘监听器
    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    # 启动监听器
    keyboard_listener.start()
    print("请按提示依次获取鼠标位置\n按\'ESC\'键退出")
    # 保持监听器活动，直到退出监听
    keyboard_listener.join()

    first_coordinates = coordinates_dict.get('first', None)
    if first_coordinates is not None and len(first_coordinates) == 0:
        print("1.请将鼠标移动到\'订单\'按钮并按下\'r\'键")

    # 停止监听器
    keyboard_listener.stop()
    print("键盘监听已停止")
    print(coordinates_dict)