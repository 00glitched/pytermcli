import os
from time import process_time
from getch import getch, pause
#py-getch

os.system("clear")

orderConf = ['\r','\t','\x7f']
# x01 ctrl + a
# x1a ctrl + z
# x1b alt + a
# x
# \x7f <- clear
# \r enter
# \t tab


def showUI():
    pass

def task(i): # tasks by ID: copy, del, new tab, etc
    os.system("clear")
    if i == 0:
        print("ENTER")
    elif i == 1:
        print("TAB")
    elif i == 2:
        print("BACKSPACE")
    else:
        print("KEYBOARD")
    showUI()


def order(key): # search key combinations
    j = 0
    for i in orderConf:
        if key == i:
            task(j)
            break
        j+=1
        if j >= len(orderConf):
            task(j)

while True: # program loop
    order(getch())
