import pyautogui as pg
import time
from plays import PLAY
from pathlib import Path
import datetime as dt
count = 1

target_image = 'img/Target.png'
cordinate = (866,562,146,92)
Sound = 1
Log = 1


def log_ss():
    path = Path("log")
    path.mkdir(parents=True, exist_ok=True)
    filename = ''.join(str(dt.datetime.now()).split(' '))
    filename = filename.replace(':','-')
    pg.screenshot(f"log/{filename}.jpg",region=cordinate)
    


def take_ss():
    pg.screenshot(target_image,region=cordinate)
    print('ss taken')
    if Log:
        log_ss()
    

while(True):
    if count==1:
        time.sleep(6)
        count+=1
        
    
    element = pg.locateOnScreen(target_image)
    print(element)
    if(element!=None):
        print('Visible')
    else:
        print('Not Visible')
        take_ss()
        if Sound:
            PLAY()
    

    
    
    

