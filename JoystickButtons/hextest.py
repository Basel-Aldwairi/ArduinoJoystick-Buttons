h = 0
x = 1023
x = x << 5
h = h ^ x
y = 512
y = y << (5+9)
h = h ^ y
print(h)