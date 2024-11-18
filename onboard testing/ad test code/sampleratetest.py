import time
import numpy as np
import ADS1256
import RPi.GPIO as GPIO

ADC = ADS1256.ADS1256()
ADC.ADS1256_init()
ADC.ADS1256_ConfigADC(0,0x82)

samples = 100

time_start = time.time_ns()
for i in range(samples):
    adc=ADC.ADS1256_GetChannalValue(0)
    time_stop = time.time_ns()

elapsed_time = time_stop-time_start

time_s = elapsed_time/np.power(10,9)
hz = samples/time_s
print(time_s)
print(hz)
