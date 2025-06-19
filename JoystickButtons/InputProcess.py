import time

import keyboard as k
import serial

ser = serial.Serial('COM5',9600, timeout = 1)
time.sleep(2)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        if not line.isnumeric():
            if not line.strip() == '' and line[0] == 'x':
                x_pos = int(line[1:])
                if x_pos > 900:
                    k.press_and_release('right')
                if x_pos < 200:
                    k.press_and_release('left')
            continue

        num = int(line)
        if num == 1:
            k.press_and_release('c')
        if num == 2:
            k.press_and_release('z')
        if num == 3:
            k.press_and_release('up')
        if num == 4:
            k.press_and_release('down')
        if num == 5:
            k.press_and_release('space')

