# 自动化模拟鼠标事件
import pyautogui
# 获取键盘事件
from pynput import keyboard

from project_modules.initial_data.initial_data import anchor_point
from project_modules.initial_data.initial_data import update_anchor_point

# 创建键盘监听器
keyboard_listener = None


def on_key_press(key):
    x, y = pyautogui.position()

    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key)
        print(key_name)

    if key_name == 'r':
        update_anchor_point(x, y)
        print("coordinate: ", x, y)
    elif key_name == 'Key.esc':
        keyboard_listener.stop()  # 停止监听器
        print(anchor_point)


def start_keyboard_listener():
    global keyboard_listener

    # 创建键盘监听器
    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    # 启动监听器
    keyboard_listener.start()
    print("键盘监听已开启，按下\'r\'键获取坐标\n按\'ESC\'键退出")

    # 保持监听器活动，直到退出监听
    keyboard_listener.join()

    # 停止监听器
    keyboard_listener.stop()
    print("键盘监听已停止")


start_keyboard_listener()
