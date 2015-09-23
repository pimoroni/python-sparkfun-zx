#!/usr/bin/env python

import zx
import time

print("""
This example will print out the recognised
X and Z positions as you move your hand
over the sensor.
""")

while True:
    if  zx.position_available():
        z, x = zx.get_position()
        print("z: {}, x: {}".format(z,x))

    time.sleep(0.01)
