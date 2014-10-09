# Import the RPi.GPIO and OS
import RPi.GPIO as GPIO
import os
import sys
import time

# GPIO port setup
GPIO.setmode(GPIO.BCM)

# Power switch: will send a shutdown message to the OS
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Reset switch: will look for a running emulator process, and send it an interrupt signal
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Mausberry circuit: when this pin goes from 1 to 0, the circuit cuts the power to the pi
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, 1)

# Looks for an emulator process and send an interrupt signal if found
def exitEmulator(channel):
    print('exitEmulator')
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

    for pid in pids:
        try:
            commandpath = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
            if commandpath[0:24] == '/opt/retropie/emulators/':
                os.system('kill -INT %s' % pid)
                print('kill -INT %s' % pid)
        except IOError:
            continue

# Sends a poweroff command to the OS
def powerOff(channel):
    print('poweroff')
    os.system('poweroff')

# Here we just wire the  GPIO inputs to their respective callback functions
GPIO.add_event_detect(23, GPIO.RISING, callback=powerOff, bouncetime=500)
GPIO.add_event_detect(25, GPIO.RISING, callback=exitEmulator, bouncetime=500)

# And... nothing more to do. let’s wait.
while True:
    time.sleep(10)
