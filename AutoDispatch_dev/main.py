# 自动化模拟鼠标事件
import pyautogui
# 获取键盘事件
from pynput import keyboard

from project_modules.getCoordinates.keyboard_listener import start_keyboard_listener
from project_modules.coordinateList import CoordinateList

start_keyboard_listener()
# # 全局变量，用于表示是否要退出监听
# exit_listener = False
# # 全局变量，用于表示是否开始执行自动点击
# start_autoclick = False
#
# def on_key_press(key):
#     global exit_listener
#
#     try:
#         key_name = key.char
#     except AttributeError:
#         key_name = str(key)
#         print(key_name)
#
#     if key_name == 'r':
#         x, y = pyautogui.position()
#         print(f"Mouse position: x={x}, y={y}")
#     elif key_name == 'Key.esc':
#         exit_listener = True
#
# # 创建键盘监听器
# keyboard_listener = keyboard.Listener(on_press=on_key_press)
#
# # 启动监听器
# keyboard_listener.start()
# print("请依次按\'r\'键获取鼠标位置")
#
# # 保持监听器活动，直到退出监听
# while not exit_listener:
#     pass
#
# # 停止监听器
# keyboard_listener.stop()
# print("程序已退出。")