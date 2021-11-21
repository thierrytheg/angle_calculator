import time
import math
from adafruit_circuitplayground.express import cpx

x0,y0,z0=cpx.acceleration[0],cpx.acceleration[1],cpx.acceleration[2]
angle_threshhold=30


def calculate_angle(x0,y0,z0,x1,y1,z1):
    num_dot_product=x0 * x1 + y0 * y1 + z0 * z1
    denom_dot_product_0=math.sqrt(x0**2 + y0**2 + z0**2)
    denom_dot_product_1=math.sqrt(x1**2 + y1**2 + z1**2)
    angle=num_dot_product/(denom_dot_product_0*denom_dot_product_1)
    angle_radian = math.acos(angle)
    angle=angle_radian*180/math.pi
    return angle


while True:
    x1,y1,z1=cpx.acceleration[0],cpx.acceleration[1],cpx.acceleration[2]
    current_angle=calculate_angle(x0,y0,z0,x1,y1,z1)
    if current_angle>angle_threshhold:
        cpx.pixels.fill((50, 0, 0))
        cpx.play_tone(800, 0.25)
        cpx.pixels.fill((0, 0, 0))


