import numpy as np
import matplotlib.pyplot as plt

data = np.load('testsave.npy')
timeseries = data[:,0]

timeseries = np.delete(timeseries, range(1000))

samplesize = np.size(timeseries)
print(samplesize)

elapsed_time = (timeseries[samplesize-1] - timeseries[0])/np.power(10,6)
hz = samplesize/elapsed_time
period = 1/hz

gapstrue = np.zeros((samplesize-1,1))
gapsperf = np.zeros((samplesize-1,1))
gapsperf[:,0] = period

for i in range(samplesize-1):
    gapstrue[i,0] = (timeseries[i+1] - timeseries[i])/np.power(10,6)

print(gapstrue)
print(np.square(np.subtract(gapstrue,gapsperf)).mean()) # MSE
