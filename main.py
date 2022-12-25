import webbrowser
import time
import keyboard

times = 0

while True:
	times += 1
	time.sleep(1)
	if times == 28800:
		urL='https://discord.com/channels/991097038382964777/1007154010085662721'
		webbrowser.get('windows-default').open_new(urL)
		time.sleep(15)
		keyboard.write("!s")
		keyboard.press_and_release("enter")
		times = 0
	print (f"{times}")
