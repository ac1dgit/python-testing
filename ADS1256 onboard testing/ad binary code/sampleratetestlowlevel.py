import time
import numpy as np
import RPi.GPIO as GPIO
import spidev
import adc

# Parameters
spi_speed_mhz = 2.5 #chip default is 20 khz
gain = adc.GAIN['1']
sample_rate = adc.DATA_RATE['100SPS']
samples = 400
channel_count = 4

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
GPIO.setup(DRDY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
SPI.max_speed_hz = int(spi_speed_mhz*np.power(10,6))
SPI.mode = 0b01

# ADS reset
GPIO.output(RST_PIN, GPIO.HIGH)
GPIO.output(RST_PIN, GPIO.LOW)
GPIO.output(RST_PIN, GPIO.HIGH)

# ID read check
adc.wait_drdy(DRDY_PIN)

GPIO.output(CS_PIN, GPIO.LOW)
SPI.writebytes([adc.CMD['RREG'] | adc.REG_DEF['STATUS'], 0x00])
id = SPI.readbytes(1)
GPIO.output(CS_PIN, GPIO.HIGH)
id = id[0] >> 4
if id == 3 :
    print("ID Read success  ")
else:
    print("ID Read failed   ")

# Config ADC
adc.wait_drdy(DRDY_PIN)

buf = [0,0,0,0,0,0,0,0]
buf[0] = (0<<3) | (1<<2) | (0<<1)
buf[1] = 0x08
buf[2] = (0<<5) | (0<<3) | (gain<<0)
buf[3] = sample_rate
GPIO.output(CS_PIN, GPIO.LOW)
SPI.writebytes([adc.CMD['WREG'] | 0, 0x03])
SPI.writebytes(buf)
GPIO.output(CS_PIN, GPIO.HIGH)

# CMD sync
GPIO.output(CS_PIN, GPIO.LOW)
SPI.writebytes([adc.CMD['SYNC']])
GPIO.output(CS_PIN, GPIO.HIGH)

# Data collection
data = np.zeros((samples,channel_count + 1))
tempvalues = np.zeros((channel_count,1))
time_start = time.time_ns()
for s in range(samples):
    for c in range(channel_count):
        # Channel select
        channel = c
        GPIO.output(CS_PIN, GPIO.LOW)
        SPI.writebytes([adc.CMD['WREG'] | adc.REG_DEF['MUX'], 0x00, (channel<<4) | (1<<3)])
        GPIO.output(CS_PIN, GPIO.HIGH)

        adc.wait_drdy(DRDY_PIN)
        # Get value
        GPIO.output(CS_PIN, GPIO.LOW)
        SPI.writebytes([adc.CMD['RDATA']])
        buf = SPI.readbytes(3)
        GPIO.output(CS_PIN, GPIO.HIGH)
        value = (buf[0]<<16) & 0xff0000
        value |= (buf[1]<<8) & 0xff00
        value |= (buf[2]) & 0xff
        if (value & 0x800000):
            value &= 0xF000000
        tempvalues[c,0] = value
    # Save values
    data[s,0] = time.time_ns()-time_start
    for c in range(channel_count):
        data[s,c+1] = tempvalues[c,0]*5.0/0x7fffff
time_stop = time.time_ns()

# Saving data table
np.save('onboard testing/ad binary code/lowleveltestsave.npy', data)
print(data)

# Result output
elapsed_time = time_stop-time_start
time_s = elapsed_time/np.power(10,9)
hz = samples/time_s
print("test duration (s):",time_s)
print("sampling rate (hz): ",hz)