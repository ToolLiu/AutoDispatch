# 复制，粘贴文本
import pyperclip
import pyautogui

def r_input(string):
    print(string)
    pyperclip.copy(string)
    pyautogui.hotkey("ctrl", "v")