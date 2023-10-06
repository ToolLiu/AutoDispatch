# 复制，粘贴文本
import pyperclip
import pyautogui

def r_input(string):
    pyperclip.copy(string)
    pyautogui.hotkey("ctrl", "v")