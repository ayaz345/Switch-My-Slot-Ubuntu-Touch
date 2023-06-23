import pyotherside
import os

prefix = 'unset LD_PRELOAD; unset LD_LIBRARY_PATH; /system/bin/bootctl '

stream = os.popen(f'{prefix}hal-info')
output = stream.read()
pyotherside.send('halVersion', output)

stream = os.popen(f'{prefix}get-number-slots')
output = stream.read()
pyotherside.send('noOfSlots', output)

stream = os.popen(f'{prefix}get-current-slot')
output = stream.read()
temp = (int(output))

if (temp == 0):
    pyotherside.send('currentSlot', "A")

elif (temp == 1):
    pyotherside.send('currentSlot', "B")

stream = os.popen(f'{prefix}get-suffix {temp}')
output = stream.read()
pyotherside.send('currentSlotSuffix', output)

def switchSlotFunc():
    if temp == 0:
        os.system(f'{prefix}set-active-boot-slot 1 && sudo reboot')
    elif temp == 1:
        os.system(f'{prefix}set-active-boot-slot 0 && sudo reboot')
