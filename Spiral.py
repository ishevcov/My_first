import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

SP_ADS = Network('SP/Spiral/Spiral_std_ads.s2p')
SP_CAD = Network('SP/Spiral/Spiral_std_cadence.s2p')

plt.figure()
SP_CAD.plot_s_db(m=1-1,    n=1-1, label='S11 Cadence', linewidth ='3')
SP_ADS.plot_s_db(m=1-1,    n=1-1, label='S11 ADS', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()

plt.figure()
SP_CAD.plot_s_smith(0,0, label='S11 Cadence', linewidth ='3',draw_labels=True)
SP_ADS.plot_s_smith(0,0, label='S11 ADS', linewidth ='3',draw_labels=True)

plt.figure()
SP_CAD.plot_s_db(m=2-1,    n=1-1, label='S21 Cadence', linewidth ='3')
SP_ADS.plot_s_db(m=2-1,    n=1-1, label='S21 ADS', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()







plt.show()