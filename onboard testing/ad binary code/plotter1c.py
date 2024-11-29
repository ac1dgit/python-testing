import numpy as np
import matplotlib.pyplot as plt

data = np.load('onboard testing/ad binary code/lowleveltestsave.npy')
print(data)

timeseries = data[:,0]/np.power(10,9)
ad0_data = data[:,1]
print(timeseries)
plt.plot(timeseries, ad0_data, color='r', label='ad 0')
plt.legend()
plt.show()