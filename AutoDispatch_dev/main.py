# 自动化模拟鼠标事件
import pyautogui
# 获取键盘事件
from pynput import keyboard

from project_modules.getCoordinates.keyboard_listener import start_keyboard_listener
from project_modules.coordinateList import CoordinateList

start_keyboard_listener()