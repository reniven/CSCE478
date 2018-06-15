import numpy as np 

features = np.genfromtxt('data/madelon.data')
labels = np.genfromtxt('data/madelon.labels')

print(isinstance(labels[0],float))
print(labels[0])
