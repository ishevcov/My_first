import skrf as rf

from skrf.calibration import TRL
from skrf.calibration import NISTMultilineTRL
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

Home_0 = 'SP/SOLT'
Home_1 = 'SP/SOLT/measurelay_1'
Home_2 = 'SP/TRL'
N_DUT = 'DUT2'

D_reflect = f'{Home_1}/open.s1p'
D_thru    = f'{Home_1}/thru.s2p'
D_Line_1 =  f'{Home_2}/Line_1.s2p'
#D_Line_2 =  f'{Home_2}/Line_2.s2p'
D_DUT_Ideal = f'{Home_0}/ideal/{N_DUT}.s2p'
D_DUT_Measure = f'{Home_1}/{N_DUT}.s2p'

reflect = rf.Network(D_reflect)



T = rf.Network(D_thru)
R = rf.two_port_reflect(reflect, reflect)
L1 = rf.Network(D_Line_1)
#L2 = rf.Network(D_Line_2)

measured = [T, R, L1]

cal = TRL(
    measured = measured,
    Grefls=[1],
    l = [0, 2.25e-3],
    gamma_root_choice = 'auto',
)

#Ideal DUT characteristic for compare
DUT_IDEAL = rf.Network(D_DUT_Ideal)

dut_raw = rf.Network(D_DUT_Measure)
dut_corrected = cal.apply_cal(dut_raw)


plt.figure()
dut_corrected.plot_s_smith(m=1 - 1, n=1 - 1, label ='Calculated DUT', linewidth='3')
DUT_IDEAL.plot_s_smith(m=1 - 1, n=1 - 1, label ='Ideal DUT', linewidth='3', linestyle='--')
plt.ylabel('S11')
plt.grid()


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

Error_21_db = 20*np.log10(dut_corrected.s[1:, 1, 0])-20*np.log10(DUT_IDEAL.s[1:, 1, 0])
F_Error = DUT_IDEAL.f[1:]
plt.figure()
plt.plot(F_Error, Error_21_db,    label='Ошибка', linewidth='3')
plt.legend()
plt.grid()

plt.show()