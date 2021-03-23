import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

SP_Ideal = Network('SP/SP_Bad_Load.s2p')
SP_FF    = Network('SP/SwitchRF12_FF_calcR.s2p')
SP_SS    = Network('SP/SwitchRF12_SS_calcR.s2p')
SP_TT    = Network('SP/SwitchRF12_TT_calcR.s2p')

plt.figure()

SP_TT.plot_s_db(m=0,    n=0, label='S11(TT)', linewidth ='3')
SP_FF.plot_s_db(m=0,    n=0, label='S11(FF)', linewidth ='3')
SP_SS.plot_s_db(m=0,    n=0, label='S11(SS)', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()

plt.figure()
SP_TT.plot_s_db(m=1,    n=0, label='S21(TT)', linewidth ='3')
SP_FF.plot_s_db(m=1,    n=0, label='S21(FF)', linewidth ='3')
SP_SS.plot_s_db(m=1,    n=0, label='S21(SS)', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()
plt.show()

