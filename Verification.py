import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network
import numpy as np
import math, cmath


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
#------------------------------------------------------------------
S_75       = Network("C:/Users/SH/Desktop/Test_1/75Ohm/75_Ohm_line.s2p")
S_75_calc  = Network("C:/Users/SH/Desktop/Test_1/75Ohm_calc.s2p")
Attenuator_6db =Network("C:/Users/SH/Desktop/Test_1/Attenuator_6db/Attenuator.s2p")
Attenuator_6db_calc =Network("C:/Users/SH/Desktop/Test_1/Attenuator_6db_calc.s2p")
Attenuator_9db =Network("C:/Users/SH/Desktop/Test_1/Attenuator_9db/Attenuator_9db.s2p")
Attenuator_9db_calc =Network("C:/Users/SH/Desktop/Test_1/Attenuator_9db_calc.s2p")
#------------------------------------------------------------------
S11_75_db = 20*np.log10(S_75.s[:, 1-1, 1-1])
S11_75_calc_db = 20*np.log10(S_75_calc.s[:, 1-1, 1-1])
S21_75_db = 20*np.log10(S_75.s[:, 2-1, 1-1])
S21_75_calc_db = 20*np.log10(S_75_calc.s[:, 2-1, 1-1])

S11_AT_6db = 20*np.log10(Attenuator_6db.s[:, 1-1, 1-1])
S11_AT_6db_calc = 20*np.log10(Attenuator_6db_calc.s[:, 1-1, 1-1])
S21_AT_6db = 20*np.log10(Attenuator_6db.s[:, 2-1, 1-1])
S21_AT_6db_calc = 20*np.log10(Attenuator_6db_calc.s[:, 2-1, 1-1])

S11_AT_9db = 20*np.log10(Attenuator_9db.s[:, 1-1, 1-1])
S11_AT_9db_calc = 20*np.log10(Attenuator_9db_calc.s[:, 1-1, 1-1])
S21_AT_9db = 20*np.log10(Attenuator_9db.s[:, 2-1, 1-1])
S21_AT_9db_calc = 20*np.log10(Attenuator_9db_calc.s[:, 2-1, 1-1])

F = S_75.f[:]
#------------------------------------------------------------------
#Plot 75
plt.figure()
plt.title("75 Ohm")
plt.plot(F, S11_75_db, label='Measure', linewidth ='3')
plt.plot(F, S11_75_calc_db, label='Calc', linewidth ='3')
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()

plt.figure()
plt.title("75 Ohm")
plt.plot(F, S21_75_db, label='Measure', linewidth ='3')
plt.plot(F, S21_75_calc_db, label='Calc', linewidth ='3')
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()
#------------------------------------------------------------------
#Plot Attenuator 6 dB
plt.figure()
plt.title("Attenuator 6 dB")
plt.plot(F, S11_AT_6db, label='Measure', linewidth ='3')
plt.plot(F, S11_AT_6db_calc, label='Calc', linewidth ='3')
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()

plt.figure()
plt.title("Attenuator 6 dB")
plt.plot(F, S21_AT_6db, label='Measure', linewidth ='3')
plt.plot(F, S21_AT_6db_calc, label='Calc', linewidth ='3')
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()
#------------------------------------------------------------------
#Plot Attenuator 9 dB
plt.figure()
plt.title("Attenuator 9 dB")
plt.plot(F, S11_AT_9db, label='Measure', linewidth ='3')
plt.plot(F, S11_AT_9db_calc, label='Calc', linewidth ='3')
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()

plt.figure()
plt.title("Attenuator 9 dB")
plt.plot(F, S21_AT_9db, label='Measure', linewidth ='3')
plt.plot(F, S21_AT_9db_calc, label='Calc', linewidth ='3')
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()

#------------------------------------------------------------------
#------------------------------------------------------------------
plt.show()
#------------------------------------------------------------------
#------------------------------------------------------------------