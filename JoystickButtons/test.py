import pyautogui
import serial
import numpy
import pyautogui as ag
from collections import deque
import threading

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
    print(f'x {x} y {y}')

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
            # print(line)
            for i in range(maxDelay - 2, -1, -1):
                keyMat[i + 1] = keyMat[i]
            keyMat[0] = numpy.zeros((1, maxButtons))
            if line.isnumeric() and int(line) != 0:

                num = int(line)
                buttons = num & (2 ** maxButtons - 1)
                x_pos = (num >> maxButtons) & (2 ** lenJSHex - 1)
                y_pos = (num >> (maxButtons + lenJSHex)) & (2 ** lenJSHex - 1)
                processJS(x_pos,y_pos)
                # print(f'b {buttons}')
                #r
                # print(num)
                for i in range(maxButtons):
                    bit = (num >> i) & 1
                    keyMat[0][i] = bit

                for i in range(maxButtons):
                    bitA = int(keyMat[0][i])
                    bitB = int(keyMat[1][i])
                    bitC = int(keyMat[1][i])
                    for j in range(2, maxDelay):
                        bitB = bitB | int(keyMat[j][i])
                        bitC = bitC & int(keyMat[j][i])
                    bitA = bitA & (((not bitB) & 1) | bitC)

                    if bitA == 1:
                        # print(f'{buttons} with {i}')
                        # print(keyMat)
                        processButton(i)

thread = threading.Thread(target=bufferProcces)
thread.start()

while True:
    if ser.in_waiting > 0:
        lineSer = ser.readline().decode('utf-8').strip()
        buffer.append(lineSer)