import numpy as np

x = np.linspace(-10, 10, 2000)
y = np.abs(x)

def chart(x, y):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(16, 16))
    plt.plot(x, y)
    plt.grid()
    plt.show()


chart(x, y)
