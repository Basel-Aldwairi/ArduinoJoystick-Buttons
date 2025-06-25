import pyautogui as ag
import numpy

max_delay = 3
max_buttons = 5

def process_button(button):
    # print(keyMat)

    button_map = {0 : 'q', 1 : 'w', 2 : 'e', 3 : 'r'}
    if button == 4:
        ag.click()
        return
    ag.press(button_map.get(button))

def process_line(line : str, key_map):

    for i in range(max_delay - 2, -1, -1):
        key_map[i + 1] = key_map[i]
    key_map[0] = numpy.zeros((1, max_buttons))

    if line.isnumeric() and int(line) != 0:
        num = int(line)

        for i in range(max_buttons):
            bit = (num >> i) & 1
            key_map[0][i] = bit

        for i in range(max_buttons):
            bit_a = int(key_map[0][i])
            bit_b = int(key_map[1][i])
            bit_c = int(key_map[1][i])
            for j in range(2, max_delay):
                bit_b = bit_b | int(key_map[j][i])
                bit_c = bit_c & int(key_map[j][i])
            bit_a = bit_a & (((not bit_b) & 1) | bit_c)

            if bit_a == 1:
                process_button(i)