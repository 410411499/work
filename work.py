import numpy as np 

samples = np.random.normal(-100,50,10000)

mean_value =np.mean(samples)
std_deviation =np.std(samples)

print("mean",mean_value)
print("standard deviation",std_deviation)