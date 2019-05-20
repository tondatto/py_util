# Implementation of Cantor pairing function
# https://en.wikipedia.org/wiki/Pairing_function
#
# cantors_pairing: 65213, 35120 --> 5033440731
# invert_cantors_pairing: 5033440731 --> 65213, 35120

import math

def cantors_pairing(x, y):
    return (((x + y + 1)*(x + y))/2) + y

def invert_cantors_pairing(z):
    w = math.floor((math.sqrt(8*z + 1)-1)/2.0)
    t = (w**2 + w)/2.0
    y = z - t
    x = w - y
    return x, y

# tests
x = [ 3, 15,  8,  7,  9]
y = [12,  7, 13,  0, 33]

z = [cantors_pairing(a, b) for a,b in zip(x,y)]

print(zip(x, y))
print(z)

for i in range(len(z)):
    print("%5d, %5d --> %5d" % (x[i], y[i], z[i]))
    
for a in z:
    print(invert_carton_pairing(a))
