#stock.py
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from songline import Sendline

token = '492THKHmNUvuBEcbSjfmdsgUm6I3NGk4atQRr8HIVuH'

messenger = Sendline(token) #messenger คือ ผู้ส่ง

def Checkprice(CODE,check=100):
    url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={}&ssoPageId=10&selectPage=2'.format(CODE)

    webopen = req(url) #req คือ เปิดเว็บโดยไม่ต้องเปิดเว็บบราวเซอร์
    page_html = webopen.read() #ข้อมูลดิบ
    webopen.close() #ปิดการ req

    data = soup(page_html,'html.parser')
    result = data.find_all('div','col-xs-6')

    #print([result[3].text])
    price = float(result[2].text)
    change = result[3].text
    change = change.replace('\n','') #replace แทน x ด้วย y
    change = change.replace('\t','')
    change = change.replace('\r','')
    change = change.replace(' ','')
    change = change.replace('เปลี่ยนแปลง','')


    pchange = result[4].text
    pchange = pchange.replace('\n','')
    pchange = pchange.replace('\r','')
    pchange = pchange.replace(' ','')
    pchange = pchange.replace('%เปลี่ยนแปลง','')

    update = data.find_all('span','stt-remark')
    update = update[0].text.replace('ข้อมูลล่าสุด','')[1:]

    print(CODE)
    print(price)
    print(change)
    print(pchange)
    print(update)
    if float(price) < check:
        messenger.sticker(5,1)
        messenger.sendimage('https://i.imgflip.com/2o9lpv.jpg')
    
    textline = 'CODE: {}\nPrice: {}\nChange: {}\n'.format(CODE,price,change)
    textline2 = '%Change: {}\nUpdate: {}'.format(pchange,update)
    messenger.sendtext(textline + textline2)
    print('------')

Checkprice('PTT',40)
Checkprice('SCB',1)

#print(len(update)) #นับว่าใน list มีข้อมูลกี่ชุด
#float() แปลงจากข้อความเป็นจุดทศนิยม
#int() แปลงจากข้อความเป็นตัวเลขจำนวนเต็ม

#print(type(price)) #คำสั่งเช็คชนิด
#print(price * 10)



