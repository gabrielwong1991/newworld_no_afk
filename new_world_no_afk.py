import pyautogui as gui
from pywinauto.application import Application
import os
import time
from random import randrange
import keyboard

# A very simple New World keep alive script #

def find_new_world():
    app = Application().connect(best_match="NewWorld", found_index=0)
    dlg = app.window(best_match="NewWorld", found_index=0)
    dlg.set_focus()

def screen_size():
    x, y = gui.size()
    return x, y
    
def gen_random(action_interval):
    rand = randrange(action_interval)
    return rand
   

def main():
    find_new_world()
    while True:
        if keyboard.is_pressed('ctrl+c'):
            break
        gui.moveTo(gen_random(x+1), gen_random(y+1))
        time.sleep(gen_random(TimeDelayBetweenAction+1))
        gui.press(keypress[gen_random(len(keypress)+1)])
    
##########################################################
# Define the action interval time #
TimeDelayBetweenAction = 5
# Change keypress to any button you want to press #
keypress = ["a", "s", "d", "f"]
x, y = screen_size()
##########################################################

if __name__ == "__main__":
    main()