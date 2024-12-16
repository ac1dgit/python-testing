import numpy as np
import matplotlib.pyplot as plt

data = np.load('onboard testing/ad binary code/lowleveltestsave.npy')
print(data)

timeseries = data[:,0]/np.power(10,9)
ad0_data = data[:,1]
ad1_data = data[:,2]
ad2_data = data[:,3]
print(timeseries)
plt.plot(timeseries, ad0_data, color='r', label='ad 0')
plt.plot(timeseries, ad1_data, color='b', label='ad 1')
plt.plot(timeseries, ad2_data, color='g', label='ad 2')
plt.legend()
plt.show()