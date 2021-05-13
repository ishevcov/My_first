import skrf as rf
from skrf.calibration import UnknownThru
from skrf.calibration import SOLT
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

# a list of Network types, holding 'ideal' responses
thru_ideal = rf.Network('SP/SOLT/ideal/thru.s2p')
short_ideal = rf.Network('SP/SOLT/ideal/short.s1p')
open_ideal =  rf.Network('SP/SOLT/ideal/open.s1p')
load_ideal =  rf.Network('SP/SOLT/ideal/load.s1p')

my_ideals = [
    rf.two_port_reflect(open_ideal, open_ideal),
    rf.two_port_reflect(short_ideal, load_ideal),
    rf.two_port_reflect(load_ideal, short_ideal),
    thru_ideal,
    ]

# a list of Network types, holding 'measured' responses
thru_measure = rf.Network('SP/SOLT/measure/thru.s2p')
short_measure = rf.Network('SP/SOLT/measure/short.s1p')
open_measure =  rf.Network('SP/SOLT/measure/open.s1p')
load_measure =  rf.Network('SP/SOLT/measure/load.s1p')

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
dut = rf.Network('SP/SOLT/measure/DUT.s2p')
dut_caled = cal.apply_cal(dut)

#Ideal DUT characteristic for compare
DUT_IDEAL = rf.Network('SP/SOLT/ideal/DUT.s2p')

# plot results
plt.figure()
dut_caled.plot_s_db(m=1 - 1, n=1 - 1, label ='Calculated DUT', linewidth='3')
DUT_IDEAL.plot_s_db(m=1 - 1, n=1 - 1, label ='Ideal DUT', linewidth='3', linestyle='--')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()

plt.figure()
dut_caled.plot_s_db(m=2 - 1, n=1 - 1, label ='Calculated DUT', linewidth='3')
DUT_IDEAL.plot_s_db(m=2 - 1, n=1 - 1, label ='Ideal DUT', linewidth='3', linestyle='--')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()

plt.show()