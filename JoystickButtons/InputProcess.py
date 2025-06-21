import time
import pyautogui as ag
import serial
import numpy

ser = serial.Serial('COM5',9600, timeout = 1)
time.sleep(2)

joystickMode = False


holdDetection = dict()
lastPressed = list()

for i in range(5):
    holdDetection[i] = 0
    lastPressed.append(0)
    lastPressed[i] = 0
prevNum = 0

while True:
    line = ser.readline().decode('utf-8').strip()
    if line.strip() == '':
        continue
    if ser.in_waiting > 0:
        if not line.isnumeric():
            x_pos = 550
            y_pos = 550
            if line[0] == 'x':
                x_pos = int(line[1:])
            if line[0] == 'y':
                y_pos = int(line[1:])
            if joystickMode:
                print()
            else:
                if x_pos > 900:
                    ag.press('right')
                if x_pos < 200:
                    ag.press('left')
                continue

        num = int(line)

        dtime = time.process_time() - lastPressed[num]
        if dtime > .5:
            holdDetection[num] = 0
        holdDetection[num] += 1
        if holdDetection[num] == 0 or holdDetection[num] > 5 or num != prevNum:
            for i in range(5):
                if i != num:
                    holdDetection[i] = 0

            if num == 1:
                ag.press('c')
            if num == 2:
                ag.press('z')
            if num == 3:
                ag.press('up')
            if num == 4:
                ag.press('down')
            if num == 0:
                ag.press('space')
        prevNum = num
