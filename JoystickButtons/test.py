import serial
import numpy
import pyautogui as ag
from collections import deque
import threading

maxDelay = 8
maxButtons = 5
keyMat = numpy.zeros((maxDelay,maxButtons))
lenJSHex = 10

ser = serial.Serial('COM5',9600,timeout=1)

def process(button):
    print(keyMat)
    if button == 0:
        ag.press('q')
     #   print(0)
    if button == 1:
        ag.press('w')
      #  print(1)
    if button == 2:
        ag.press('e')
       # print(2)
    if button == 3:
        ag.press('r')
        # print(3)
    if button == 4:
        ag.press('t')
        # print(4)

buffer = deque(maxlen=1)

def bufferProcces():
    while True:

        for line in list(buffer):
            print(line)
            for i in range(maxDelay - 2, -1, -1):
                keyMat[i + 1] = keyMat[i]
            keyMat[0] = numpy.zeros((1, maxButtons))
            if line.isnumeric() and int(line) != 0:

                num = int(line)
                buttons = num & (2 ** maxButtons - 1)
                x_pos = (num >> maxButtons) & (2 ** lenJSHex - 1)
                y_pos = (num >> (maxButtons + lenJSHex)) & (2 ** lenJSHex - 1)
                # print(f'b {buttons}')
                # print(f'x {x_pos}')
                # print(f'y {y_pos}')
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
                        process(i)

thread = threading.Thread(target=bufferProcces)
thread.start()

while True:
    if ser.in_waiting > 0:
        lineSer = ser.readline().decode('utf-8').strip()
        buffer.append(lineSer)