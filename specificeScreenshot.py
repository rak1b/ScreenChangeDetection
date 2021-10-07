
               #Rakib






import pyautogui as pg
element = pg.locateOnScreen('img/settings.PNG')
print(element)
pg.screenshot('test.png',region=(element.left,element.top,element.width,element.height))