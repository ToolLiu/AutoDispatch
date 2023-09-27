# 获取键盘事件
from pynput import keyboard
def on_key_press(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key)
        print(key_name)

    if key_name == 'Key.esc':
        keyboard_listener.stop()  # 停止监听器

def if_exit_listener():
    global keyboard_listener

    # 创建键盘监听器
    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    # 启动监听器
    keyboard_listener.start()
    print("程序执行完毕，按\'ESC\'键退出")
    # 保持监听器活动，直到退出监听
    keyboard_listener.join()

    # 停止监听器
    keyboard_listener.stop()