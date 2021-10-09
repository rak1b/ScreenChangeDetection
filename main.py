import pyautogui as pg
import time
from pathlib import Path
import datetime as dt
import os
from playsound import playsound



#Take a screenshot of the target place and put the location here
target_image = 'img/target.png'

#Find the cordinate by using the Getlocation.py file
cordinate = (881,555,117,100)

#time to excute code after running the program
wait = 6


#If you don't want sound in each changes then,replace  Sound = 0
Sound = 1

#If you don't want Log in each changes then,replace  Log = 0
Log = 1





count = 1
def log_ss():
    '''
    This function takes the screenshot whenever 
    the targetted place changes
    and store them in the log folder
    '''
    path = Path("log")
    path.mkdir(parents=True, exist_ok=True)
    filename = ''.join(str(dt.datetime.now()).split(' '))
    filename = filename.replace(':','-')
    pg.screenshot(f"log/{filename}.jpg",region=cordinate)
    
def PLAY():
    #Play sound 
    playsound(os.getcwd()+'/sound/'+'Error.mp3')

def take_ss():
    #Takes screenshot on specifice location
    pg.screenshot(target_image,region=cordinate)
    print('ss taken')
    if Log:
        log_ss()
        
def press_button():
    '''
    press f2
    after 0.5s
    press ctrl
    after 0.2s
    Press b
    '''
    pg.press('f2')
    time.sleep(0.5)
    
    pg.press('ctrl')
    time.sleep(0.2)
    
    pg.press('b')
    print('button pressed')
    

    
try:
    while(True):
        if count==1:
            time.sleep(wait)
            count+=1
            
        
        element = pg.locateOnScreen(target_image)
        if(element!=None):
            print('Visible')
        else:
            print('Not Visible')
            press_button()
            if Sound:
                PLAY()
            take_ss()
            
except KeyboardInterrupt:
    print("Code Stopped")
    

    
    
    

