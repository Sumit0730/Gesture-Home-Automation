VERSION = (1, 0, 2, 'final', 0)


def get_version():
    "Returns a PEP 386-compliant version number from VERSION."
    assert len(VERSION) == 5
    assert VERSION[3] in ('alpha', 'beta', 'rc', 'final')
    
    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|c}N - for alpha, beta and rc releases
    
    parts = 2 if VERSION[2] == 0 else 3
    main = '.'.join(str(x) for x in VERSION[:parts])
    
    sub = ''
    
    if VERSION[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'rc'}
        sub = mapping[VERSION[3]] + str(VERSION[4])
    
    return str(main + sub)

from pyfirmata import Arduino, util
from tkinter import *
import board
import tone
import simpleio

comport = 'COM9'
global fan
root= Tk()
board = Arduino(comport)
buzzer = board.digital[11]
TONE_FREQ = [ 262, 294, 330, 349, 392, 440, 494 ]
buzzer.frequency = TONE_FREQ[0]
buzzer.duty_cycle = 2**15

iter8= util.Iterator(comport)
iter8.start()

led_1 = board.digital[13]
led_2 = board.digital[12]

def move_servo(angle):
    fan.write(angle)

def led(total):
    if total == 0:
        led_1.write(1)
        led_2.write(1)

    elif total == 1:
        led_1.write(0)
        led_2.write(0)

    elif total == 2:
        led_1.write(1)
        led_2.write(1)
    elif total == 3:
        led_1.write(0)
        led_2.write(0)

    elif total == 4:
        led_1.write(1)
        led_1.write(1)
    elif total == 5:
        led_1.write(0)
        led_2.write(0)
    return None


