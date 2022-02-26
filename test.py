import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(100)
y = np.random.random(100)

plt.plot(np.sort(x)[::-1],y)
plt.xlabel('x')
plt.ylabel('y')