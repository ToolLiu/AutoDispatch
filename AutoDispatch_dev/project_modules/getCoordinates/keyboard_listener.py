# 自动化模拟鼠标事件
import pyautogui
# 获取键盘事件
from pynput import keyboard

from .coordinates import coordinates_dict, update_coordinates

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

    if key_name == '1':
        update_coordinates("订单", x, y)
        print("2.请将鼠标移动到\'抢单\'按钮并按下\'2\'键")
    elif key_name == '2':
        update_coordinates("抢单", x, y)
        print("3.请将鼠标移动到搜索框并按下\'3\'键")
    elif key_name == '3':
        update_coordinates("搜索", x, y)
        print("4.请将鼠标移动到\'查询\'键并按下\'4\'键")
    elif key_name == '4':
        update_coordinates("查询", x, y)
        print("字典录入完成！清按ESC退出并执行程序。")
    elif key_name == 'Key.esc':
        keyboard_listener.stop()  # 停止监听器

def start_keyboard_listener():
    global keyboard_listener

    # 创建键盘监听器
    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    # 启动监听器
    keyboard_listener.start()
    print("请按提示依次获取鼠标位置\n按\'ESC\'键退出")
    print("1.请将鼠标移动到\'订单\'按钮并按下\'1\'键")
    # 保持监听器活动，直到退出监听
    keyboard_listener.join()

    # 停止监听器
    keyboard_listener.stop()
    print("键盘监听已停止")
    print("坐标字典：", coordinates_dict)