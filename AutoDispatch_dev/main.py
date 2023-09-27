# main

from project_modules.getCoordinates.keyboard_listener import start_keyboard_listener
from project_modules.autoClick.autoClick import start_auto_click
from project_modules.exitScript.exitScript import if_exit_listener

start_keyboard_listener()
start_auto_click()
if_exit_listener()
