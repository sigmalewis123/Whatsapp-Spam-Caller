import pyautogui
import time
import os


call_icon_path = "C:\\Users\\sigma\\Pictures\\Screenshots\\Screenshot 2025-01-24 195343.png"
hangup_icon_path = "c:\\Users\\sigma\\Pictures\\Screenshots\\Screenshot 2025-01-24 200214.png"

def locate_and_click(image_path, confidence=0.9):
    print(f"Looking for image at {image_path}...")
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            print(f"Found {image_path}, clicking at {location}.")
            pyautogui.click(location)
            return True
        else:
            print(f"{image_path} not found on screen.")
    except pyautogui.ImageNotFoundException as e:
        print(f"Error: {e}")
    return False

if not os.path.exists(call_icon_path):
    print("Call  image nonexistent!")
if not os.path.exists(hangup_icon_path):
    print("Hangup image nonexistent!")

try:
    while True:
        print("Looking for call icon...")
        if locate_and_click(call_icon_path, confidence=0.9):
            time.sleep(1) 
            print("Looking for hangup icon...")
            locate_and_click(hangup_icon_path, confidence=0.9)  
            time.sleep(2)  
        else:
            print("Call icon not found. Retrying in 2 seconds...")
            time.sleep(2)  

        time.sleep(0.5)  

except KeyboardInterrupt:
    print("Script terminated.")
