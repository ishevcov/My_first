import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network
import numpy as np


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

Folder_1   = f"SP/Calibration/Calibration_10mm.s2p"
Legend_1 = "L=10мм"
Folder_2   = f"SP/Calibration/Calibration_50mm.s2p"
Legend_2 = "L=50мм"

SP_10 = Network(Folder_1)
SP_50 = Network(Folder_2)

plt.figure()
SP_10.plot_s_db(m=1 - 1, n=1 - 1, label = Legend_1, linewidth='3')
SP_50.plot_s_db(m=1 - 1, n=1 - 1, label = Legend_2, linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()


plt.figure()
SP_10.plot_s_db(m=2 - 1, n=1 - 1, label = Legend_1, linewidth='3')
SP_50.plot_s_db(m=2 - 1, n=1 - 1, label = Legend_2, linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()




plt.show()