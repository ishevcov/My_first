import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network
import numpy as np


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"



Title   = "1.5 мкм"
Folder_1   = f"SP/Chip_Line/Chip_Line_Accuracy/Three_lines_15um.s12p"
Legend_1   = "50 мкм"
Legend_2   = "100 мкм"
Legend_3   = "200 мкм"

SP = Network(Folder_1)
SP.se2gmm(6)

plt.figure()
plt.title(Title)
SP.plot_s_db(m=1 - 1, n=1 - 1, label= Legend_1, linewidth='3')
SP.plot_s_db(m=3 - 1, n=3 - 1, label= Legend_2, linewidth='3')
SP.plot_s_db(m=5 - 1, n=5 - 1, label= Legend_3, linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.legend()
plt.grid()

plt.figure()
plt.title(Title)
SP.plot_s_smith(m=1 - 1, n=1 - 1, label=Legend_1, linewidth='3',  draw_labels=True)
SP.plot_s_smith(m=3 - 1, n=3 - 1, label=Legend_2, linewidth='3',  draw_labels=True)
SP.plot_s_smith(m=5 - 1, n=5 - 1, label=Legend_3, linewidth='3',  draw_labels=True)


plt.figure()
plt.title(Title)
SP.plot_s_db(m=2 - 1, n=1 - 1, label= Legend_1, linewidth='3')
SP.plot_s_db(m=4 - 1, n=3 - 1, label= Legend_2, linewidth='3')
SP.plot_s_db(m=6 - 1, n=5 - 1, label= Legend_3, linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.legend()
plt.grid()




plt.show()

