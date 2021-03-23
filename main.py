# library
import numpy as np
import matplotlib.pyplot as plt



plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

x = np.linspace(0, 3, 100)
plt.plot(x, x,    label='Линейная')  #
plt.plot(x, x**2, label='Квадратная', linewidth='2',   linestyle='--')
plt.plot(x, x**3, label='Кубическая', color = 'green', linestyle='-.')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()





'''





'''