import skrf as rf
from skrf.calibration import UnknownThru
from skrf.calibration import SOLT
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

def PLOT_db(Data, label='Test', N_fig = 1, sp = 11):
    plt.figure(N_fig)
    First = int(sp/10)
    Second = sp - First*10
    Data.plot_s_db(m=First - 1, n=Second - 1, label=label, linewidth='3')
    plt.ylabel(f'S{sp}, дБ')
    plt.xlabel('F, Гц')

def PLOT_smith(Data, label='Test', N_fig = 1, sp = 11):
    plt.figure(N_fig)
    First = int(sp/10)
    Second = sp - First*10
    Data.plot_s_smith(m=First - 1, n=Second - 1, label=label, linewidth='3')
    plt.ylabel(f'S{sp}')

#Folder Files
Home_ideal = 'SP/SOLT/ideal'
Home_measure = 'SP/SOLT/measureLay_con'
N_DUT = 'DUT2'
N_Load = 'load.s1p'


D_short_i   = f'{Home_ideal}/short.s1p'
D_open_i    = f'{Home_ideal}/open.s1p'
D_load_i    = f'{Home_ideal}/{N_Load}'
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
dut_calc = cal.apply_cal(dut)

#Ideal DUT characteristic for compare
DUT_IDEAL = rf.Network(D_DUT_Ideal)

#plot DATA
PLOT_smith(dut_calc, sp =11, label='Calculated DUT', N_fig=1)
PLOT_smith(DUT_IDEAL, sp =11, label='Ideal DUT', N_fig=1)
plt.grid()

PLOT_db(dut, sp =11, label='Measure DUT', N_fig=2)
PLOT_db(dut_calc, sp =11, label='Calculated DUT', N_fig=2)
PLOT_db(DUT_IDEAL, sp =11, label='Ideal DUT', N_fig=2)
plt.grid()

PLOT_db(dut, sp =21, label='Measure DUT', N_fig=3)
PLOT_db(dut_calc, sp =21, label='Calculated DUT', N_fig=3)
PLOT_db(DUT_IDEAL, sp =21, label='Ideal DUT', N_fig=3)
plt.grid()

Error_21_db = 20*np.log10(dut_calc.s[:, 1, 0])-20*np.log10(DUT_IDEAL.s[:, 1, 0])
F_Error = DUT_IDEAL.f[:]
plt.figure()
plt.plot(F_Error, Error_21_db,    label='Ошибка', linewidth='3')
plt.legend()
plt.grid()

plt.show()