import pyautogui as pg
import time

target_image = 'img/target.png'

time.sleep(6)
locate = pg.locateOnScreen(target_image)
print(f'({locate.left},{locate.top},{locate.width},{locate.height})')