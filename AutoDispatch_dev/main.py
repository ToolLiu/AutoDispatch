# main

from project_modules.get_coordinates.keyboard_listener import start_keyboard_listener
from project_modules.auto_click.auto_click import start_auto_click
from project_modules.exit_script.exit_script import if_exit_listener

start_keyboard_listener()
start_auto_click()
if_exit_listener()
