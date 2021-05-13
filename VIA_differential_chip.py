import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network
import numpy as np


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


Folder_1   = f"SP/Chip_VIA/Chip_VIA_2.s4p"
Title = "L= 100 мкм"

SP = Network(Folder_1)
SP.se2gmm(2)

plt.figure()
SP.plot_s_db(m=1 - 1, n=1 - 1, label = 'VIA', linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()

plt.figure()
SP.plot_s_db(m=2 - 1, n=1 - 1, label = 'VIA', linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()



plt.show()