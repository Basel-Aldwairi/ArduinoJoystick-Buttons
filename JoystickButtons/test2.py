import serial
import numpy
import pyautogui as ag

maxDelay = 5
maxButtons = 5
lenJSHex = 10
keyMat = numpy.zeros((maxDelay,maxButtons))

ser = serial.Serial('COM5',9600,timeout=1)


while True:
    if ser.in_waiting > 0:

        line = ser.readline().decode('utf-8').strip()
        if line.isnumeric():
            num = int(line)
            buttons = num & (2**maxButtons - 1)
            x_pos = (num >> (maxButtons )) & (2**(lenJSHex) - 1 )
            y_pos = (num >> (maxButtons + lenJSHex)) & (2**(lenJSHex) - 1 )
            print(f'b {buttons}')
            print(f'x {x_pos}')
            print(f'y {y_pos}')
        else:
            print(line)