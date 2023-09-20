import matplotlib.pyplot as plt
import numpy as np

start = 0
end = 2 * np.pi
step = 0.001
x = np.arange(start, end + step, step)
y = np.sin(x)
plt.plot(x, y)
plt.grid()
plt.show()
