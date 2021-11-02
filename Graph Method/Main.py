import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5.0, 5.0, 0.1)
y = x**3 - 2*(x**2) + 6*x - 4
plt.plot(x,y,'-')
plt.xlabel('X'); plt.ylabel('Y'); plt.grid(True)
plt.show()
