import skrf as rf
from skrf.calibration import UnknownThru
from skrf.calibration import SOLT
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#Folder Files

Home_ideal = 'SP/SOLT/ideal'
Home_measure = 'SP/SOLT/measureLay_1'
N_DUT = 'DUT2'

D_short_i   = f'{Home_ideal}/short.s1p'
D_open_i    = f'{Home_ideal}/open.s1p'
D_load_i    = f'{Home_ideal}/load_L.s1p'
D_thru_i    = f'{Home_ideal}/thru.s2p'
D_DUT_Ideal = f'{Home_ideal}/{N_DUT}.s2p'

D_short_m   = f'{Home_measure}/short.s1p'
D_open_m    = f'{Home_measure}/open.s1p'
D_load_m    = f'{Home_measure}/load.s1p'
D_thru_m    = f'{Home_measure}/thru.s2p'
D_DUT_Measure = f'{Home_measure}/{N_DUT}.s2p'


# a list of Network types, holding 'ideal' responses
short_ideal = rf.Network(D_short_i)
open_ideal =  rf.Network(D_open_i)
load_ideal =  rf.Network(D_load_i)
thru_ideal = rf.Network(D_thru_i)

my_ideals = [
    rf.two_port_reflect(open_ideal, open_ideal),
    rf.two_port_reflect(short_ideal, load_ideal),
    rf.two_port_reflect(load_ideal, short_ideal),
    thru_ideal,
    ]

# a list of Network types, holding 'measured' responses
short_measure = rf.Network(D_short_m)
open_measure =  rf.Network(D_open_m)
load_measure =  rf.Network(D_load_m)
thru_measure = rf.Network(D_thru_m)

my_measured = [
    rf.two_port_reflect(open_measure, open_measure),
    rf.two_port_reflect(short_measure, load_measure),
    rf.two_port_reflect(load_measure, short_measure),
    thru_measure,
    ]

## create a SOLT instance
cal = SOLT(
    ideals = my_ideals,
    measured = my_measured,
    )

# run calibration algorithm
cal.run()

# apply it to a dut
dut = rf.Network(D_DUT_Measure)
dut_caled = cal.apply_cal(dut)


#Ideal DUT characteristic for compare
DUT_IDEAL = rf.Network(D_DUT_Ideal)






plt.figure()
dut_caled.plot_s_smith(m=1 - 1, n=1 - 1, label ='Calculated DUT', linewidth='3')
DUT_IDEAL.plot_s_smith(m=1 - 1, n=1 - 1, label ='Ideal DUT', linewidth='3', linestyle='--')
plt.ylabel('S11')
plt.grid()

plt.figure()
dut_caled.plot_s_db(m=1 - 1, n=1 - 1, label ='Calculated DUT', linewidth='3')
DUT_IDEAL.plot_s_db(m=1 - 1, n=1 - 1, label ='Ideal DUT', linewidth='3', linestyle='--')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()



plt.figure()
dut_caled.plot_s_db(m=2 - 1, n=1 - 1, label='Calculated DUT', linewidth='3')
DUT_IDEAL.plot_s_db(m=2 - 1, n=1 - 1, label='Ideal DUT', linewidth='3', linestyle='--')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()


Error_21_db = 20*np.log10(dut_caled.s[:, 1, 0])-20*np.log10(DUT_IDEAL.s[:, 1, 0])
F_Error = DUT_IDEAL.f[:]
plt.figure()
plt.plot(F_Error, Error_21_db,    label='Ошибка', linewidth='3')
plt.legend()
plt.grid()





plt.show()