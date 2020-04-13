import time
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.5

while True:
    cpx.pixels.fill((0, 20, 100))
    for i in range(10):
        num = i * 3
        cpx.pixels[i] = (0, 20+ num, 70)
    for i in range(10):
        num = i * 3
        cpx.pixels[i] = (0, 50+ num, 60)
    for i in range(10):
        num = i * 3
        cpx.pixels[i] = (0, 40 + num, 50)
    for i in range(10):
        num = i * 3
        cpx.pixels[i] = (0, 30 + num, 40)
    time.sleep(1)
