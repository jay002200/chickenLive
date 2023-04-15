# chickenLive

## 簡介
看老外很多養雞直播，最近自己也有養雞，也跟著紀錄雞的生活。  
使用自動化更新資訊在直播上顯示。
```
https://www.youtube.com/@user-tn1lb5cg3o
```
<img src="https://github.com/jay002200/chickenLive/blob/main/live.png">


### 抓取產蛋量：
從Google Sheet抓取產蛋量，顯示在畫面上，crontab定時30分鐘抓一次。
使用opencv將數量寫在圖片上。  
<img src="https://github.com/jay002200/chickenLive/blob/main/egg.jpg">

### 天氣
使用Wttr.in，使用crontab，定時執行並存成圖片。
```
wget -N wttr.in/zhunan_0q_lang=zh.png -O zhunan.png
```

### 聊天室指令控制
在聊天室輸入指令，可控制鏡頭位置，和小米電燈。
目前指令:
```  
!closelight or !關燈  
!openlight or !開燈  
!上 or !up  
!下 or !down  
!右 or !right  
!左 or !left  
```

### device
synology vvm (Ubuntu 22.04)  
Cam: Tp-link C210
