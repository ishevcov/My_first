import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network
import numpy as np


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"




Folder_1   = f"SP/Chip_Via_Line/Via_Line_Chip.s4p"
Title = "L= 100 мкм"
SP = Network(Folder_1)
SP.se2gmm(2)

plt.figure()
plt.title(Title)
SP.plot_s_db(m=1 - 1, n=1 - 1, label = 'VIA+Line', linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()

plt.figure()
plt.title(Title)
SP.plot_s_db(m=2 - 1, n=1 - 1, label = 'VIA+Line', linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()



plt.show()