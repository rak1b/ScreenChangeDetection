import pyautogui as pg
import time

target_image = 'img/Target.png'

time.sleep(6)
locate = pg.locateOnScreen(target_image)
print(f'({locate.left},{locate.top},{locate.width},{locate.height})')