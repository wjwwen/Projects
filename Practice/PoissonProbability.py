import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

k = np.arange(0, 17)

print(k)

pmf = poisson.pmf(k, mu=7)
pmf = np.round(pmf, 5)

print(pmf)

for val, prob in zip(k,pmf):
    print(f"k-value {val} has probability = {prob}")
    
plt.plot(k, pmf, marker='o')
plt.xlabel('k')
plt.ylabel('Probability')

plt.show()