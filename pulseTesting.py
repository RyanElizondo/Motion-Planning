#!/usr/bin/env python3

from servoControl import servo_controlTEST
from pinControl import pin_setup, pin_clean


pin_setup()


inp = input('Enter pulse \n')
servo_controlTEST(int(inp))

pin_clean()
