import webbrowser
import pyautogui as pg # pg คือตัวย่อของ package
import time
import pyperclip

def Search(keyword = 'ประเทศไทย',eng = False):
    # 1-open webbrowser (google)
    url = 'https://www.google.com'
    webbrowser.open(url) #เปิดเว็บไซต์
    time.sleep(3)
    # 2-type keyword
    if eng == True:
        pg.write(keyword,interval=0.25)
    else:
        pyperclip.copy(keyword) # ก็อปปี้ลงคลิปบอร์ด เหมือนกด ctrl+c
        time.sleep(0.5)
        pg.hotkey('ctrl','v') #ห้ามใช้เครื่องหมายบวก
    time.sleep(1)
    # 3-press enter
    pg.press('enter')
    time.sleep(3)
    # 4-screenshot
    pg.screenshot( keyword + '.png')

Search('ราคาทองคำ')
Search('bcc news',eng=True)
Search('ราคาน้ำมัน')













#กรณีต้องการเปิด browser โดยตรง
#from subprocess import Popen
#path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#Popen(path)
