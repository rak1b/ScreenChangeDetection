import pyautogui as pg
import time
from plays import play
count = 1
while(True):
    
    if count==1:
        time.sleep(1)
        count+=1
    
    element = pg.locateOnScreen('img/test.PNG')
    print(element)
    if(element!=None):
        print('Visible')
    else:
        print('Not Visible')
        play()
#         pg.press('winleft')
    
# import keyboard

# while(True):
#     print('running')
#     # if keyboard.is_pressed('a'):
#     #     print("A pressed")
#     #     break
#     keyboard.wait('esc')
    # break
    
    
    

