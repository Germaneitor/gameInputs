from pyautogui import hotkey, keyDown, keyUp, locateOnScreen, screenshot
from skimage.metrics import structural_similarity as compare_ssim
import cv2
import time
import sys
import numpy as np

def main():
    time.sleep(1)
    startgame()
        
def startgame():
    softreset()
    for i in range(2):
        keyDown('enter')
        keyUp('enter')
        time.sleep(3)
    keyDown('x')
    keyUp('x')
    time.sleep(3)
    select_pokemon()

def softreset():
    #hotkey(('enter', 'space', 'q', 'w'))
    keyDown('enter')
    keyDown('space')
    keyDown('q')
    keyDown('w')
    keyUp('enter')
    keyUp('space')
    keyUp('q')
    keyUp('w')
    time.sleep(9)

def select_pokemon():
    keyDown('x')
    keyUp('x')
    time.sleep(3)
    for poke in ['totodile.png', 'cyndaquil.png', 'chikorita.png']:
        keyDown('l')
        keyUp('l')
        time.sleep(1)
        check_pokemon(poke) # maybe conditional to stop program here
    # soft reset emulator to keep checking
    with open('total_resets.txt', 'w') as resets:
            resets.write(str(TOTAL_SOFT_RESETS))
    resets.close()

def check_pokemon(poke_img):
    global TOTAL_SOFT_RESETS
    # create image variable for pokemon to compare
    # screenshot('images/' + poke_img, (0,60,513,355))
    pokemon = cv2.imread('images/' + poke_img)
    # look for it in screen with locateOnScreen
    # print(locateOnScreen(pokemon))
    screenshot('images/shiny.png', (0,60,513,355))
    shiner = cv2.imread('images/shiny.png')
    score = compare_ssim(pokemon, shiner, channel_axis=2)
    if score < 0.99:
        with open('total_resets.txt', 'w') as resets:
            resets.write(str(TOTAL_SOFT_RESETS))
        resets.close()
        sys.exit('Might be a shiny!!')
    else:
        TOTAL_SOFT_RESETS += 1

if __name__ == "__main__":
    hotkey('alt', 'tab')
    global TOTAL_SOFT_RESETS
    with open('total_resets.txt', 'r') as resets:
        TOTAL_SOFT_RESETS = int(resets.readline())
    resets.close()
    while True:
        main()