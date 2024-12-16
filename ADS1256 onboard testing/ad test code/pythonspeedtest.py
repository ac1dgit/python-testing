import time
import numpy as np

hztarget = 60000

samples = 30000
data = np.zeros((samples,2))

t=time.time()
period=1/hztarget

time_start = time.time_ns()

for i in range(samples):
    t+=period
    data[i,:] = [time.time_ns(), 12345]
    time.sleep(max(0,t-time.time()))
time_stop = time.time_ns()

print(data)

elapsed_time = time_stop-time_start
time_s = elapsed_time/np.power(10,9)
hz = samples/time_s
print(time_s)
print(hz)
