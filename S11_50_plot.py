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

plt.figure()
plt.plot(Zin, S11_db,    label='S11')
plt.plot(Test_Load[0], S11_db[Test_50],  "ro", label = "R=50", color = 'green')
plt.plot(Test_Load[1], S11_db[Test_100], "ro", label = "R=100", color = 'red')
plt.plot(Test_Load[2], S11_db[Test_200], "ro", label = "R=200", color = 'blue')
plt.plot(Test_Load[3], S11_db[Test_400], "ro", label = "R=400", color = 'tomato')
plt.plot(Test_Load[4], S11_db[Test_800], "ro", label = "R=800", color = 'hotpink')
print(S11_db[Test_50])
plt.xlabel('ZL, Ом')
plt.xscale("log")
plt.ylabel('S11, дБ')
plt.grid()
plt.legend()



Vtn = 0.3
Cox = 7.6e-3
Cov = 289e-12
unCox = 187e-6
L = 100e-9
Vgs = 1.2

Vds = 0
F = 30e9

W = np.linspace(5e-6, 16e-6, 100)
R_switch = L/(unCox*W*(Vgs-Vtn-Vds))
Cgs = W*L*Cox*0.5+W*Cov
R_C_tot = 1/(2*3.14*F*Cgs)

plt.figure()
plt.plot(W, R_switch,    label='R')
plt.xlabel('W, м')
plt.ylabel('R, Ом')
plt.grid()

fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('W, м')
plt.grid()
ax1.set_ylabel('Сdg, Ф', color=color)
ax1.plot(W, Cgs, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('R(30ГГц), Ом', color=color)  # we already handled the x-label with ax1
ax2.plot(W, R_C_tot, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.grid()
plt.show()







