import skrf as rf
from skrf.calibration import UnknownThru
from skrf.calibration import TRL
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

reflect = rf.Network('SP/TRL/Reflect.s1p')

T = rf.Network('SP/TRL/Thru.s2p')
R = rf.two_port_reflect(reflect, reflect)
L1 = rf.Network('SP/TRL/Line_1.s2p')
L2 = rf.Network('SP/TRL/Line_2.s2p')

measured = [T, R, L2]

cal = TRL(
    measured = measured,
    Grefls=[1],
    l = [0, 7.5e-3],
    gamma_root_choice = 'auto',
)

#Ideal DUT characteristic for compare
DUT_IDEAL = rf.Network('SP/TRL/DUT_ideal.s2p')

dut_raw = rf.Network('SP/TRL/DUT.s2p')
dut_corrected = cal.apply_cal(dut_raw)


plt.figure()
dut_corrected.plot_s_db(m=1 - 1, n=1 - 1, label ='Calculated DUT', linewidth='3')
DUT_IDEAL.plot_s_db(m=1 - 1, n=1 - 1, label ='Ideal DUT', linewidth='3', linestyle='--')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()


plt.figure()
dut_corrected.plot_s_db(m=2 - 1, n=1 - 1, label ='Calculated DUT', linewidth='3')
DUT_IDEAL.plot_s_db(m=2 - 1, n=1 - 1, label ='Ideal DUT', linewidth='3', linestyle='--')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()



plt.show()