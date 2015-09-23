# Python Library for Sparkfun ZX Distance/Gesture Sensor

Get one here: https://shop.pimoroni.com/products/zx-distance-and-gesture-sensor

## Installing

Run `make` if you have it, to install for Python 2 and 3.

Alternatively:

```
sudo python3 setup.py install
```

## Usage

* `gesture_available` - Returns `True` if a gesture is available
* `position_available` - Returns `True` if a position ( Z and X coordinates ) is available
* `get_x` - Returns the X position
* `get_z` - Returns the Z position
* `get_position` - Returns the Z and X position, use like so: `Z, X = zx.get_position()`
* `get_gesture` - Returns a gesture, if there is one, otherwise returns none. Available gestures are:
    * zx.SWIPE_LEFT
    * zx.SWIPE_RIGHT
    * zx.SWIPE_UP
* `get_speed` - Returns the speed of the gesture
* `gesture_name( gesture )` - Accepts a gesture number and returns the text name of a gesture ( ie: "Swipe Left" )

Here's a simple example that prints out the Z and X positions:

```python
import zx
import time

while True:
    if zx.position_available():
        z, x = zx.get_position()
        print("z: {}, x: {}".format(z,x))
    time.sleep(0.01)
```
