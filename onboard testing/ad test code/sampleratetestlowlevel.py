import time
import numpy as np
import RPi.GPIO as GPIO
import spidev

# Pin definition
SPI = spidev.SpiDev(0, 0)
RST_PIN = 18
CS_PIN = 22
DRDY_PIN = 17

# Module init
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RST_PIN, GPIO.OUT)
GPIO.setup(CS_PIN, GPIO.OUT)
#GPIO.setup(DRDY_PIN, GPIO.IN)
GPIO.setup(DRDY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
SPI.max_speed_hz = 2000000 #default is 20000
SPI.mode = 0b01 # default is 0b01

# ADS reset
GPIO.output(RST_PIN, GPIO.HIGH)
time.sleep(200 // 1000.0)
GPIO.output(RST_PIN, GPIO.LOW)
time.sleep(200 // 1000.0)
GPIO.output(RST_PIN, GPIO.HIGH)

# ID read check
for i in range(0,400000,1):
    if(GPIO.input(DRDY_PIN) == 0):
        break
    if(i >= 400000):
        print ("Time Out ...\r\n")

GPIO.output(CS_PIN, GPIO.LOW)
SPI.writebytes([0x10 | 0, 0x00])
id = SPI.readbytes(1)
GPIO.output(CS_PIN, GPIO.HIGH)
id = id[0] >> 4
if id == 3 :
    print("ID Read success  ")
else:
    print("ID Read failed   ")

# Config ADC
for i in range(0,400000,1):
    if(GPIO.input(DRDY_PIN) == 0):
        break
    if(i >= 400000):
        print ("Time Out ...\r\n")
buf = [0,0,0,0,0,0,0,0]
gain = 0
drate = 0xF0
buf[0] = (0<<3) | (1<<2) | (0<<1)
buf[1] = 0x08
buf[2] = (0<<5) | (0<<3) | (gain<<0)
buf[3] = drate
GPIO.output(CS_PIN, GPIO.LOW)
SPI.writebytes([0x50 | 0, 0x03])
SPI.writebytes(buf)
GPIO.output(CS_PIN, GPIO.HIGH)
time.sleep(1 // 1000.0)

# Data collection prep
hztarget = 5000
samples = 1000
data = np.zeros((samples,2))
t=time.time()
period=1/hztarget
time_start = time.time_ns()

 # Channel select
channel = 0
GPIO.output(CS_PIN, GPIO.LOW)
SPI.writebytes([0x50 | 1, 0x00, (channel<<4) | (1<<3)])
GPIO.output(CS_PIN, GPIO.HIGH)

# CMD sync
GPIO.output(CS_PIN, GPIO.LOW)
SPI.writebytes([0xFC])
GPIO.output(CS_PIN, GPIO.HIGH)

# CMD wakeup
GPIO.output(CS_PIN, GPIO.LOW)
SPI.writebytes([0x00])
GPIO.output(CS_PIN, GPIO.HIGH)

# Data collection
for s in range(samples):
    # Cycle time logging
    t+=period

    # DRDY WAIT
    for i in range(0,400000,1):
        if(GPIO.input(DRDY_PIN) == 0):
            break
        if(i >= 400000):
            print ("Time Out ...\r\n")
    # Get value
    GPIO.output(CS_PIN, GPIO.LOW)
    SPI.writebytes([0x01])
    buf = SPI.readbytes(3)
    GPIO.output(CS_PIN, GPIO.HIGH)
    value = (buf[0]<<16) & 0xff0000
    value |= (buf[1]<<8) & 0xff00
    value |= (buf[2]) & 0xff
    if (value & 0x800000):
        value &= 0xF000000
   
    # Save value
    data[s,:] = [time.time_ns(),value*5.0/0x7fffff]

    # Cycle time align
    time.sleep(max(0,t-time.time()))
time_stop = time.time_ns()

# Saving data table
np.save('lowleveltestsave.npy', data)
print(data)

# Result output
elapsed_time = time_stop-time_start
time_s = elapsed_time/np.power(10,9)
hz = samples/time_s
print("test duration (s):",time_s)
print("sampling rate (hz): ",hz)