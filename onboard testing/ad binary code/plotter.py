import numpy as np
import matplotlib.pyplot as plt

data = np.load('saved data/testsave.npy')
print(data)

timeseries = data[:,0]
ad0_data = data[:,1]
ad1_data = data[:,2]
print(timeseries)
plt.plot(timeseries, ad0_data, color='r', label='ad 0')
plt.plot(timeseries, ad1_data, color='b', label='ad 1')
plt.legend()
plt.show()