import time
import numpy as np
import ADS1256
import RPi.GPIO as GPIO

ADC = ADS1256.ADS1256()
ADC.ADS1256_init()
ADC.ADS1256_ConfigADC(0,0xF0)
#'ADS1256_30000SPS' : 0xF0
#'ADS1256_15000SPS' : 0xE0
#'ADS1256_7500SPS' : 0xD0
#'ADS1256_3750SPS' : 0xC0
#'ADS1256_2000SPS' : 0xB0
#'ADS1256_1000SPS' : 0xA1
#'ADS1256_500SPS' : 0x92
#'ADS1256_100SPS' : 0x82
#'ADS1256_60SPS' : 0x72
#'ADS1256_50SPS' : 0x63
#'ADS1256_30SPS' : 0x53
#'ADS1256_25SPS' : 0x43
#'ADS1256_15SPS' : 0x33
#'ADS1256_10SPS' : 0x20
#'ADS1256_5SPS' : 0x13
#'ADS1256_2d5SPS' : 0x03

hztarget = 1000

samples = 5000
data = np.zeros((samples,3))

t=time.time()
period=1/hztarget

time_start = time.time_ns()

for i in range(samples):
    t+=period
    data[i,:] = [time.time_ns(),ADC.ADS1256_GetChannalValue(0)*5.0/0x7fffff,ADC.ADS1256_GetChannalValue(1)*5.0/0x7fffff]
    time.sleep(max(0,t-time.time()))
time_stop = time.time_ns()

np.save('testsave.npy', data)
print(data)

elapsed_time = time_stop-time_start
time_s = elapsed_time/np.power(10,9)
hz = samples/time_s
print(time_s)
print(hz)