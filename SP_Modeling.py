import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

SP = Network('SP/FR4_1UM.s2p')


plt.figure()
SP.plot_s_db(m=2-1, n=1-1, label='S21', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()

plt.figure()
SP.plot_s_db(m=1-1, n=1-1, label='S11', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()

plt.figure()
SP.plot_s_smith(0,0, label='S11', linewidth ='3',draw_labels=True)

plt.show()

