# SOS program using onboard LED

from machine import Pin
import utime


p25LED = machine.Pin(25,machine.Pin.OUT)

# ensure LED is off on start
p25LED.value(0)
utime.sleep(3)

# set unit time for morse code
unit_time = 0.5

while True:
    # print S (...)
    for i in range(3):
        p25LED.toggle()
        utime.sleep(unit_time)
        p25LED.toggle()
        utime.sleep(unit_time)

    # print O (---)
    for i in range(3):
        p25LED.toggle()
        utime.sleep(3 * unit_time)
        p25LED.toggle()
        utime.sleep(unit_time)

    # print S (...)
    for i in range(3):
        p25LED.toggle()
        utime.sleep(unit_time)
        p25LED.toggle()
        utime.sleep(unit_time)

    # print word end
    utime.sleep(7 * unit_time)
