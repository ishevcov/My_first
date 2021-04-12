import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network
import numpy as np


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


SP_FF   = Network('SP/PEX_ONE_RF12_FF.s2p')
SP_SS   = Network('SP/PEX_ONE_RF12_SS.s2p')
SP_TT   = Network('SP/PEX_ONE_RF12_TT.s2p')
SP_Ideal =Network('SP/SP_Bad_Load.s2p')


S21_TT_db = 20*np.log10(SP_TT.s[:, 1, 0])
S21_FF_db = 20*np.log10(SP_FF.s[:, 1, 0])
S21_SS_db = 20*np.log10(SP_SS.s[:, 1, 0])
S21_Ideal_db = 20*np.log10(SP_Ideal.s[:, 1, 0])
F = SP_TT.f[:]
Error_FF = S21_Ideal_db-S21_FF_db
Error_SS = S21_Ideal_db-S21_SS_db
Error_TT = S21_Ideal_db-S21_TT_db


plt.figure()
plt.title("PEX")
plt.plot(F, -Error_SS, label='SS', linewidth ='3')
plt.plot(F, Error_TT, label='TT', linewidth ='3')
plt.plot(F, -Error_FF, label='FF', linewidth ='3')
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('Error, дБ')
plt.grid()

plt.figure()
plt.title("PEX")
SP_SS.plot_s_db(m=1-1, n=1-1, label='SS', linewidth ='3')
SP_TT.plot_s_db(m=1-1, n=1-1, label='TT', linewidth ='3')
SP_FF.plot_s_db(m=1-1, n=1-1, label='FF', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()

plt.figure()
plt.title("PEX")
SP_SS.plot_s_db(m=2-1, n=1-1, label='SS', linewidth ='3')
SP_TT.plot_s_db(m=2-1, n=1-1, label='TT', linewidth ='3')
SP_FF.plot_s_db(m=2-1, n=1-1, label='FF', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()


plt.show()