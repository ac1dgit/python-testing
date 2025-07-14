import numpy as np
import csv
import matplotlib.pyplot as plt

data = []
with open("MCC118 onboard testing/logs/2025_July_14_183629.csv") as csvfile:
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
ad4_data = data[:,4]
ad5_data = data[:,5]
ad6_data = data[:,6]
ad7_data = data[:,7]
print(timeseries)
plt.plot(timeseries, ad0_data, color='r', label='ad 0')
plt.plot(timeseries, ad1_data, color='b', label='ad 1')
plt.plot(timeseries, ad2_data, color='g', label='ad 2')
plt.plot(timeseries, ad3_data, color='C0', label='ad 3')
plt.plot(timeseries, ad4_data, color='C1', label='ad 4')
plt.plot(timeseries, ad5_data, color='c', label='ad 5')
plt.plot(timeseries, ad6_data, color='C6', label='ad 6')
plt.plot(timeseries, ad7_data, color='C10', label='ad 7')
plt.legend()
plt.show()