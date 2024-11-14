import numpy as np
import time

start = time.time()

size1 = 8
size2 = 10

A = np.zeros((size1,size2))

print(A)
count = 1

for s1 in range(size1):
    for s2 in range(size2):
        A[s1,s2] = count
        count += 1

print(A)

end = time.time()
print(end - start)

# works on pi 14/11/2024