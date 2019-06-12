import pyautogui
import pyperclip

def capture_screen_data():
    #Click Name of Mushroom
    pyautogui.click(43,84, duration=0.3 )
    #High light text

    pyautogui.moveTo(492, 57, duration=0.3 )
    pyautogui.dragTo(1426, 818, button='left', duration=0.3 )

    #Copy
    pyautogui.hotkey('ctrl', 'c')

    #Click Close
    pyautogui.click(1400,819, duration=0.3)

    #Scroll down
    pyautogui.click(468, 805, duration=0.3)

    #paste
    text = pyperclip.paste()

    #Write text to file
    mushroomData = open('mushroom_data.txt' ,'a')
    mushroomData.write(text)
    mushroomData.close()

i = 0
for i in range(5) :
    capture_screen_data()
