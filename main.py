#import一些東西
import webbrowser #import webbrowser
import time #import time
import keyboard #import keyboard

#變數設定
times = 0 #時間的變數
urL='https://nafstore.net/account' #設定開啟的網址

#不斷重複
while True: #就是我讓這裡不會停的
	times += 1 #把times +1
	time.sleep(1) #等一秒Code也是會累的
	if times == 86410: #如果時間過了24小時+10秒(避免與網站計時不同)
		webbrowser.get('windows-default').open_new(urL) #開啟https://nafstore.net/account
		times = 0 #重製時間
	print (f"{times}") #顯示現在經過幾秒
