import pytchat
from pytapo import Tapo
import subprocess
import os
from miio import Yeelight
import signal
import time
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
import datetime
import pygsheets

def getliveid():
    auth_file = "-.json"
    gc = pygsheets.authorize(service_file = auth_file)   
    # setting sheet
    sheet_url = "https://docs.google.com/spreadsheets/d/-" 
    sheet = gc.open_by_url(sheet_url)
    sheet_test01 = sheet.worksheet_by_title("工作表1")
    videoid = sheet_test01.cell("S2")
    return videoid.value
def open():
    client = mqtt.Client()
    client.connect("-", 1883, 60)
    time.sleep(1)
    client.publish("-", "-")
    
def close():
    client = mqtt.Client()
    client.connect("-", 1883, 60)
    time.sleep(1)
    client.publish("-", "-")

videoid = getliveid()
chat = pytchat.create(video_id="{0}".format(videoid))

        

camera = Tapo("-", "-", "-")
pid = os.getpid()

drink = False

while 1:
    try:
        for c in chat.get().sync_items():
            name = c.author.name
            message = c.message
            print(f"{c.datetime} [{c.author.name}]- {c.message}")
            if message == "!左" or message == "!left":
                try:
                    camera.moveMotor(-5, 0)
                except:
                    print("已到最底")
            if message == "!右" or message == "!right":
                try:
                    camera.moveMotor(5, 0)
                except:
                    print("已到最底")
            if message == "!上" or message == "!up":
                try:
                    camera.moveMotor(0, 5)
                except:
                    print("已到最底")
            if message == "!下" or message == "!down":
                try:
                    camera.moveMotor(0, -5)
                except:
                    print("已到最底")
            if message == "!開燈" or message == "!openlight":
                yeelight = Yeelight("-", "-")
                yeelight.on()
            if message == "!關燈" or message == "!closelight":
                yeelight = Yeelight("-", "-")
                yeelight.off()
            if message == "!開電扇":
                open()
            if message == "!關電扇":
                close()
    except:
        print("Error.Reconnected")
        subprocess.call(['python3', '/home/chicken/youtube.py', str(pid)])
        os.kill(os.getpid(),signal.SIGKILL)
    
    now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
    hours = now.strftime('%H')
    
    if hours == "00" and drink == False:
        drink = True
        yeelight = Yeelight("-", "-")
        yeelight.on()
        time.sleep(180)
        yeelight.off() 
    
    if hours != "00":
        drink = False
