import numpy as np
import matplotlib.pyplot as plt

data = np.load('testsave.npy')

timeseries = data[:,0]
samplesize = np.size(timeseries)
elapsed_time = data[samplesize-1,0] - data[0,0]
hz = samplesize/elapsed_time
period = 1/hz

gapstrue = np.zeros((samplesize,1))
gapsperf = np.zeros((samplesize,1))
gapsperf[:,0] = period

for i in range(samplesize-1):
    gapstrue[i,0] = timeseries[i+1] - timeseries[i]

print(gapstrue)
print(gapsperf)

print(np.square(np.subtract(gapstrue,gapsperf)).mean()) # MSE
