import time
import pyautogui
import random

pyautogui.FAILSAFE = False

try:
    x_range, y_range = (500, 1000), (200, 600)
    
    while True:
        x, y = random.randint(*x_range), random.randint(*y_range)
        pyautogui.moveTo(x, y, duration=0.01)
        print("Mouse moved to:", x, y)
        
        time.sleep(random.uniform(0.5, 1.5)) 
        pyautogui.press('shift')
        print("Shift key pressed")
        
        time.sleep(random.uniform(3, 5)) 

except KeyboardInterrupt:
    print("mouse mover stopped")
