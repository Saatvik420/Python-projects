import pyautogui as p
import time

limit= (10)
message = ("https://cdn.discordapp.com/attachments/946690557592346664/946690771556372490/image0.gif")
i = 0
time.sleep(3)
while i<int(limit):

    p.typewrite(message)
    p.press("enter")
    i+=1