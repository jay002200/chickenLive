import pytchat
from pytapo import Tapo
import subprocess
import os
from miio import Yeelight
import signal

chat = pytchat.create(video_id="--") #youtube直播網址
camera = Tapo("192.168.-", "account", "pwd") #Tapo攝影機的IP 帳號 密碼 如果登不進去 試試帳號改用admin
pid = os.getpid()


while 1:
    try:
        for c in chat.get().sync_items():
            name = c.author.name
            message = c.message
            print(f"{c.datetime} [{c.author.name}]- {c.message}")
            if message == "!左" or message == "!left":
                try:
                    camera.moveMotor(-15, 0)
                except:
                    print("已到最底")
            if message == "!右" or message == "!right":
                try:
                    camera.moveMotor(15, 0)
                except:
                    print("已到最底")
            if message == "!上" or message == "!up":
                try:
                    camera.moveMotor(0, 15)
                except:
                    print("已到最底")
            if message == "!下" or message == "!down":
                try:
                    camera.moveMotor(0, -15)
                except:
                    print("已到最底")
            if message == "!開燈" or message == "!openlight":
                yeelight = Yeelight("IP", "token") #小米電燈
                yeelight.on()
            if message == "!關燈" or message == "!closelight":
                yeelight = Yeelight("IP", "token") #小米電燈
                yeelight.off()
    except AttributeError: #如果抓不到youtube聊天室 重啟程式再抓一次
        print("Error.Reconnected")
        subprocess.call(['python3', '/1.py', str(pid)])
        os.kill(os.getpid(),signal.SIGKILL)