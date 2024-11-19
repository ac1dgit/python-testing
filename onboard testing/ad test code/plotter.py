import numpy as np
import matplotlib.pyplot as plt

data = np.load('testsave.npy')
print(data)

xpoints = data[:,0]
ypoints = data[:,1]
print(xpoints)
plt.plot(xpoints, ypoints)
plt.show()