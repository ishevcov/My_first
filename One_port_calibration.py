import skrf as rf
from skrf.calibration import OnePort
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"



# a list of Network types, holding 'ideal' responses
my_ideals = [\
        rf.Network('SP/One_port/ideal/short.s1p'),
        rf.Network('SP/One_port/ideal/open.s1p'),
        rf.Network('SP/One_port/ideal/load.s1p'),
        ]

# a list of Network types, holding 'measured' responses

my_measured = [\
        rf.Network('SP/One_port/measure/short.s1p'),
        rf.Network('SP/One_port/measure/open.s1p'),
        rf.Network('SP/One_port/measure/load.s1p'),
        ]

## create a Calibration instance
cal = rf.OnePort(\
        ideals = my_ideals,
        measured = my_measured,
        )

## run, and apply calibration to a DUT

# run calibration algorithm
cal.run()

# apply it to a dut
dut = rf.Network('SP/One_port/measure/DUT.s1p')
dut_caled = cal.apply_cal(dut)


#Ideal DUT characteristic for compare
DUT_IDEAL = rf.Network('SP/One_port/ideal/DUT.s1p')

# plot results
dut_caled.plot_s_db(m=1 - 1, n=1 - 1, label ='Calculated DUT', linewidth='3')
DUT_IDEAL.plot_s_db(m=1 - 1, n=1 - 1, label ='Ideal DUT', linewidth='3', linestyle='--')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()
plt.show()





