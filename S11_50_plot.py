# library
import numpy as np
import matplotlib.pyplot as plt
import math



plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

max = 1000
min = 1
N_points = 400
Zin = np.linspace(1, 1000, 400)
Delta = (max-min)/N_points

Test_Load = np.array([50, 100, 200, 400, 800])

Test_50 = int(50/(999/400))
Test_100 = int(100/(999/400))
Test_200 = int(200/(999/400))
Test_400 = int(400/(999/400))
Test_800 = int(800/(999/400))
Rs = 50
S11 = np.abs((Zin-Rs)/(Zin+Rs))
S11_db = 20*np.log10(S11)


plt.plot(Zin, S11_db,    label='S11')
plt.plot(Test_Load[0], S11_db[Test_50],  "ro", label = "R=50", color = 'green')
plt.plot(Test_Load[1], S11_db[Test_100], "ro", label = "R=100", color = 'red')
plt.plot(Test_Load[2], S11_db[Test_200], "ro", label = "R=200", color = 'blue')
plt.plot(Test_Load[3], S11_db[Test_400], "ro", label = "R=400", color = 'tomato')
plt.plot(Test_Load[4], S11_db[Test_800], "ro", label = "R=800", color = 'hotpink')
print(S11_db[Test_50])
plt.xlabel('Zin, Ом')
plt.xscale("log")
plt.ylabel('S11, дБ')
plt.grid()
plt.legend()
plt.show()