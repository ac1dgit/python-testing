import time
import numpy as np
import ADS1256
import RPi.GPIO as GPIO

ADC = ADS1256.ADS1256()
ADC.ADS1256_init()
ADC.ADS1256_ConfigADC(0,0xF0)

hztarget = 2000

samples = 30000
data = np.zeros((samples,2))

t=time.time()
period=1/hztarget

time_start = time.time_ns()

for i in range(samples):
    t+=period
    data[i,:] = [time.time_ns(),ADC.ADS1256_GetChannalValue(7)*5.0/0x7fffff]
    time.sleep(max(0,t-time.time()))
time_stop = time.time_ns()

np.save('testsave.npy', data)
print(data)

elapsed_time = time_stop-time_start
time_s = elapsed_time/np.power(10,9)
hz = samples/time_s
print(time_s)
print(hz)
