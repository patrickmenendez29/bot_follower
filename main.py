import time
import pyautogui


def follow(count=1):
    # countdown before program starts
    time.sleep(5)
    # follow button position: 1094, 443
    #15 px from top to first follow button
    #25px per button
    #30px button size
    for _ in range(count):
        # move to follow button
        pyautogui.moveTo(1094, 443)

        #click to follow
        pyautogui.click()

        # move to optional cancel
        pyautogui.moveTo(1132, 703)
        # click to cancel
        pyautogui.click()

        #25 + 30 for a full button scroll
        #840, 690 position to cancel
        #Scroll -66 to make it a perfect scroll
        pyautogui.scroll(-66)
    pass








def unfollow(count):
    for _ in range(count):
        time.sleep(2)
    pass

def is_pending():
    if pyautogui.locateOnScreen('pendiente.png') == (1038,417,92,49):
        return True
    return False

def is_followed():
    if pyautogui.locateOnScreen('siguiendo.png') == (1038,417,92,49):
        return True
    return False

def advanced_follow(count):
    x_pos = 1150

    for _ in range(count):
        time.sleep(5)


        pyautogui.moveTo(x_pos, 301)
        pyautogui.click()
        pyautogui.moveTo(x_pos, 360)
        pyautogui.click()

        pyautogui.moveTo(x_pos, 420)
        pyautogui.click()

        pyautogui.moveTo(x_pos, 480)
        pyautogui.click()

        pyautogui.moveTo(x_pos, 530)
        pyautogui.click()

        pyautogui.moveTo(x_pos, 580)
        pyautogui.click()

        pyautogui.moveTo(x_pos, 640)
        pyautogui.click()

        pyautogui.moveTo(x_pos, 700)
        pyautogui.click()

        pyautogui.moveTo(x_pos, 760)
        pyautogui.click()

        pyautogui.moveTo(x_pos, 815)
        pyautogui.click()

        pyautogui.moveTo(x_pos, 870)
        pyautogui.click()

        pyautogui.moveTo(x_pos, 917)
        pyautogui.click()

        pyautogui.moveTo(962, 933)
        pyautogui.dragTo(955,297,1)






if __name__ == '__main__':
    advanced_follow(10)