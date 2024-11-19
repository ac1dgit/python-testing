import time
import numpy as np
import matplotlib.pyplot as plt
import ADS1256
import RPi.GPIO as GPIO

ADC = ADS1256.ADS1256()
ADC.ADS1256_init()
ADC.ADS1256_ConfigADC(0,0xB2)

samples = 3000
data = np.zeros((samples,2))

time_start = time.time_ns()
for i in range(samples):
    data[i,:] = [(time.time_ns()-time_start)/np.power(10,6),ADC.ADS1256_GetChannalValue(0)*5.0/0x7fffff]
time_stop = time.time_ns()

np.save('testsave.npy', data)
print(data)

elapsed_time = time_stop-time_start
time_s = elapsed_time/np.power(10,9)
hz = samples/time_s
print(time_s)
print(hz)
