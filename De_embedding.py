import skrf as rf
from skrf import Network
import matplotlib.pyplot as plt
import numpy as np

def VNA_Error(SP):
    for i in range(len(SP)):
        if abs(SP.s[i, 1, 0]) >= 1:
            SP.s[i, 1, 0] = SP.s[i - 1, 1, 0]

        if abs(SP.s[i, 0, 0]) >= 1:
            SP.s[i, 0, 0] = SP.s[i - 1, 0, 0]

        if abs(SP.s[i, 1, 1]) >= 1:
            SP.s[i, 1, 1] = SP.s[i - 1, 1, 1]

        if abs(SP.s[i, 0, 1]) >= 1:
            SP.s[i, 0, 1] = SP.s[i - 1, 0, 1]


SP_W = Network('SP/De_embedding/W_DUT.s2p')
SP_WO = Network('SP/De_embedding/WO_DUT.s2p')

VNA_Error(SP_W)
VNA_Error(SP_WO)


plt.figure()
SP_WO.plot_s_db(m= 0, n= 0, label= 'With', linewidth='3')
SP_WO.plot_s_db(m= 1, n= 0, label= 'With', linewidth='3')
SP_WO.plot_s_db(m= 1, n= 1, label= 'With', linewidth='3')
SP_WO.plot_s_db(m= 0, n= 1, label= 'With', linewidth='3')
plt.grid()


DUT = rf.de_embed(SP_WO, SP_W)

plt.figure()

DUT.plot_s_db(m=2 - 1, n=1 - 1, label= 'Legend', linewidth='3')
plt.grid()


plt.show()