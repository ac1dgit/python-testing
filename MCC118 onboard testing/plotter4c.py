import numpy as np
import csv
import matplotlib.pyplot as plt

data = []
with open("MCC118 onboard testing/logs/diode test.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        data.append(row)

data = np.array(data)
hz = 3000
period = 1/hz
datasize = np.size(data,0)
timeseries = np.zeros((datasize,1))
s = 0
for time in range(datasize):
    timeseries[time,0] = s
    s += period
ad0_data = data[:,0]
ad1_data = data[:,1]
ad2_data = data[:,2]
ad3_data = data[:,3]
print(timeseries)
plt.plot(timeseries, ad0_data, color='r', label='ad 0')
plt.plot(timeseries, ad1_data, color='b', label='ad 1')
plt.plot(timeseries, ad2_data, color='g', label='ad 2')
plt.plot(timeseries, ad3_data, color='C0', label='ad 3')
plt.legend()
plt.show()