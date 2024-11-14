To set up and run this Python script, here’s a step-by-step guide for a beginner:

Step 1: Install Python
Download Python: Go to python.org/downloads and download the latest version for your operating system (Windows, macOS, or Linux).
Install Python: Run the installer. During installation, check the box that says “Add Python to PATH” before clicking Install. This will allow you to run Python from the command line easily.
Step 2: Install Required Libraries
Open Command Prompt or Terminal:
On Windows, press Win + R, type cmd, and press Enter.
On macOS, open Terminal from the Applications folder.
Install pyautogui Library:
Type the following command and press Enter:
bash

pip install pyautogui
This installs pyautogui, a library used to control the mouse and keyboard.
Step 3: Set Up the Python Script
Open a Text Editor: Use a simple text editor like Notepad on Windows, TextEdit on macOS, or a code editor like Visual Studio Code (VSCode).

Copy the Code: Copy the Python code below:

python

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
    print("Mouse mover stopped")


Save the File:

Save the file with a name like mouse_movement.py.
Make sure to save it with the .py extension (e.g., mouse_movement.py).
Step 4: Run the Script
Open Command Prompt or Terminal:

Navigate to the folder where you saved mouse_movement.py using the command cd <path to folder>. For example:
bash
cd Downloads
Run the Script:

Type the following command and press Enter:
bash
python mouse_movement.py     (for windows)
python3 mouse_movement.py    (for mac)
The script will start moving your mouse and pressing the Shift key at intervals.

Step 5: Stop the Script
To Stop the Script: Press Ctrl + C in the terminal or Command Prompt where the script is running. This triggers the KeyboardInterrupt, and you should see the message “mouse mover stopped.”
Important Notes
Fail-Safe: pyautogui.FAILSAFE = False is set to prevent the program from stopping if you move the mouse to the screen’s corner. If you want to add this feature back, set pyautogui.FAILSAFE = True.
