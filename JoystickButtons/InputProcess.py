import pyautogui
import serial
import numpy
import pyautogui as ag
from collections import deque
import threading
import processButtons

maxDelay = 8
maxButtons = 5
keyMat = numpy.zeros((maxDelay,maxButtons))
lenJSHex = 10
JSMode = True

ser = serial.Serial('COM5',9600,timeout=1)

def processButton(button):
    # print(keyMat)

    buttonMap = {0 : 'q', 1 : 'w', 2 : 'e', 3 : 'r'}
    if button == 4:
        ag.click()
        return
    ag.press(buttonMap.get(button))

buffer = deque(maxlen=1)

def processJS(x,y):

    if JSMode:
        x_new = 0
        y_new = 0
        if x > 812:
            x_new = 40
        elif x <= 812 and x > 512:
            x_new= 20
        elif x < 212:
            x_new = - 40
        elif x >= 212 and x < 512:
            x_new = -20
        if y > 812:
            y_new = 40
        elif y <= 812 and y > 512:
            y_new = 20
        elif y < 212:
            y_new = -40
        elif y >= 212 and y < 512:
            y_new = -20
        ag.moveRel(x_new, y_new)
    else:
        if x > 512:
            ag.press('right')
        elif x < 512:
            ag.press('left')
        if y > 512:
            ag.press('down')
        elif y < 512:
            ag.press('up')


def bufferProcces():
    while True:

        for line in list(buffer):
            # print(line)qweqwe
            processButtons.process_line(line,keyMat)

            if line.isnumeric() and int(line) != 0:

                num = int(line)
                buttons = num & (2 ** maxButtons - 1)
                x_pos = (num >> maxButtons) & (2 ** lenJSHex - 1)
                y_pos = (num >> (maxButtons + lenJSHex)) & (2 ** lenJSHex - 1)
                processJS(x_pos,y_pos)
                # print(f'b {buttons}')
                #r
                # print(num)

thread = threading.Thread(target=bufferProcces)
thread.start()

while True:
    if ser.in_waiting > 0:
        lineSer = ser.readline().decode('utf-8').strip()
        buffer.append(lineSer)