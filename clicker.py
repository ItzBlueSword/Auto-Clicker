import time
import threading
import tkinter as tk
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="t")
SPEED_UP_KEY = KeyCode(char="u")
SPEED_DOWN_KEY = KeyCode(char="d")

clicking = False
mouse = Controller()
click_speed = 0.007  # Initial click speed

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(click_speed)

def toggle_event(key):
    global clicking
    global click_speed

    if key == TOGGLE_KEY:
        clicking = not clicking
    elif key == SPEED_UP_KEY:
        click_speed -= 0.001  # Decrease click speed by 0.001 seconds
    elif key == SPEED_DOWN_KEY:
        click_speed += 0.001  # Increase click speed by 0.001 seconds

def create_gui():
    def speed_up():
        global click_speed
        click_speed -= 0.001

    def speed_down():
        global click_speed
        click_speed += 0.001

    root = tk.Tk()
    root.title("Auto Clicker")

    speed_up_button = tk.Button(root, text="Speed Up", command=speed_up)
    speed_up_button.pack()

    speed_down_button = tk.Button(root, text="Speed Down", command=speed_down)
    speed_down_button.pack()

    root.mainloop()

click_thread = threading.Thread(target=clicker)
click_thread.start()

gui_thread = threading.Thread(target=create_gui)
gui_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
