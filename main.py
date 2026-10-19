import keyboard
import pyautogui
import time

# toggle mouse click on key
def holdClick():
    # prevents action on repeat key press
    clicking = False

    while True:
        # press down
        if keyboard.is_pressed('[') and not clicking:
            pyautogui.mouseDown()
            clicking = True

        # release
        if keyboard.is_pressed(']') and clicking:
            pyautogui.mouseUp()
            clicking = False

        # performance wait
        time.sleep(0.01)


# main
if __name__ == '__main__':
    holdClick()
