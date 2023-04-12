import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pygsheets
import datetime


def make_egg_pic(text1,text2,text3):
    text = "今日蛋蛋:"
    text += text1
    allegg = "全部蛋蛋:"
    allegg += text2
    time = "更新時間:\n"
    time += text3
    img = cv2.imread("/home/-")
    imgPil = Image.fromarray(img)
    fontPath = "/home/-"
    font = ImageFont.truetype(fontPath,110)
    draw = ImageDraw.Draw(imgPil)
    draw.text((93,37),text,font=font,fill=(255,0,255))
    draw.text((93,152),allegg,font=font,fill=(255,0,255))
    font = ImageFont.truetype(fontPath,55)
    draw.text((93,288),time,font=font,fill=(255,0,255))
    img = np.array(imgPil)
    path = "/home/test/egg.jpg"
    cv2.imwrite(path,img)
    
def googlesheet():
    
    now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
    hours = now.strftime('%H')
    
    auth_file = "/home/-"
    gc = pygsheets.authorize(service_file = auth_file)   
    # setting sheet
    sheet_url = "https://docs.google.com/-" 
    sheet = gc.open_by_url(sheet_url)
    sheet_test01 = sheet.worksheet_by_title("工作表1")
    
    #new day new egg
    if hours == "00":
    	sheet_test01.update_value("O2","0")
     
    O2 = sheet_test01.cell('O2')  #今日產蛋
    P2 = sheet_test01.cell('P2')  #總蛋量
    Q2 = sheet_test01.cell('Q2')  #更新時間
    data = []
    data.append(O2.value)
    data.append(P2.value)
    data.append(Q2.value)
    
    
    return data

data = googlesheet()
todayegg = str(data[0])
allegg = str(data[1])
time = str(data[2])
make_egg_pic(todayegg,allegg,time)
