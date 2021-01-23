import pulseio
import board
import time
import touchio
from digitalio import DigitalInOut, Direction, Pull
from planetsong import song
from notes import notes

# init buttons
touch1 = touchio.TouchIn(board.A0)
touch2 = touchio.TouchIn(board.A1)
touch3 = touchio.TouchIn(board.A2)

# init LEDs
ledG = DigitalInOut(board.D5)
ledG.direction = Direction.OUTPUT
ledR = DigitalInOut(board.D6)
ledR.direction = Direction.OUTPUT
ledB = DigitalInOut(board.D7)
ledB.direction = Direction.OUTPUT

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

# turn red = calibration

ledR.value = True
ledG.value = True
ledB.value = True

# init PWMs

pwmspk1 = pulseio.PWMOut(board.D1, duty_cycle=0x7fff, frequency=440, variable_frequency=True)

mapping = ["C3","D3","E3","F3","G3","A3","B3"]

while True:
    v = 0
    if touch1.raw_value > 2200:
        v = v|0x01
        ledR.value = False
    if touch2.raw_value > 2200:
        v = v|0x02
        ledG.value = False
    if touch3.raw_value > 2200:
        v = v|0x04
        ledB.value = False
    if v > 0:
        pwmspk1.frequency = int(round(notes[mapping[v-1]]))
        pwmspk1.duty_cycle = 0x7fff
    else:
        pwmspk1.duty_cycle = 0
        ledR.value = True
        ledG.value = True
        ledB.value = True
