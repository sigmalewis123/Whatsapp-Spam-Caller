##YOU'll NEED TO UPDATE THE IMAGE PATH YOURSELF IN THE CODE

# Auto Call Answer and Hangup Script

This Python script automates the process of answering and hanging up a call by searching for specific icons on the screen and clicking them. It continuously checks for the icons and clicks on them when found, with retry logic in case the icons are not immediately found.

## Features

- Searches for the **call icon** and clicks on it to answer the call.
- After answering, searches for the **hangup icon** and clicks on it to end the call.
- Retries continuously if the icons are not found, with configurable waiting times.
- Can be used for automating call actions in applications with graphical interfaces.

## Requirements

- **Python 3.x** (tested with Python 3.13)
- **PyAutoGUI**: For screen automation and image recognition.
- **OpenCV**: Required for image matching and recognition with confidence levels.

### Install Dependencies

To install the required libraries, use the following command:

```bash
pip install pyautogui opencv-python
