import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network
import numpy as np
import math, cmath


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

SP_single  = Network("SP/Test_diff/SD_line.s4p")
SP_diff = Network("C:/Users/SH/Desktop/one_diff/diff.s2p")
SP_one_port = Network("C:/Users/SH/Desktop/Test_1/Results_Final.s2p")

S11_one_db = 20*np.log10(SP_one_port.s[:, 1-1, 1-1])
S21_one_db = 20*np.log10(SP_one_port.s[:, 2-1, 1-1])
F2 = SP_one_port.f[:]

S11_db = 20*np.log10(SP_diff.s[:, 1-1, 1-1])
S21_db = 20*np.log10(SP_diff.s[:, 2-1, 1-1])
F1 =  SP_diff.f[:]

Sdd11_single = 0.5*(SP_single.s[:, 1-1, 1-1]-SP_single.s[:, 1-1, 3-1]-SP_single.s[:, 3-1, 1-1]+SP_single.s[:, 3-1, 3-1])
Sdd21_single = 0.5*(SP_single.s[:, 2-1, 1-1]-SP_single.s[:, 4-1, 1-1]-SP_single.s[:, 2-1, 3-1]+SP_single.s[:, 4-1, 3-1])

Sdd11_single_db=20*np.log10(Sdd11_single)
Sdd21_single_db=20*np.log10(Sdd21_single)

F = SP_single.f[:]


plt.figure()
plt.plot(F1, S11_db, label='Measure', linewidth ='3')
#plt.plot(F, Sdd11_single_db, label='Calculate', linewidth ='3',linestyle='--')
plt.plot(F2, S11_one_db, label='One Port', linewidth ='3',linestyle='--')


plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()


plt.figure()
plt.title("PEX")
plt.plot(F1, S21_db, label='Measure', linewidth ='3')
#plt.plot(F, Sdd21_single_db, label='Calculate', linewidth ='3',linestyle='--')
plt.plot(F2, S21_one_db, label='One Port', linewidth ='3',linestyle='--')


plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()

plt.show()