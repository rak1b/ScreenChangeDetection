import pyautogui as pg
import time

target_image = 'img/target.png'

time.sleep(6)
try:
    locate = pg.locateOnScreen(target_image)
    print(f'({locate.left},{locate.top},{locate.width},{locate.height})')
except:
    print("\nFailed to locate the image you are looking for..\n")
    print('HINT:Just open the window that you want to search ')