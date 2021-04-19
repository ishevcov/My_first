import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network
import numpy as np
import math, cmath
from scipy import linalg

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#Интересные функции numpy
#https://pythonworld.ru/numpy/4.html
#example
#https://github.com/scikit-rf/scikit-rf/issues/235

#----------------------------------------------------------
#Input Data
#----------------------------------------------------------

S_75 = Network("C:/Users/SH/PycharmProjects/Course_Python_Django/SP/Two_ports/Reference_75_DUT.s2p")
Cascade = Network("C:/Users/SH/PycharmProjects/Course_Python_Django/SP/Two_ports/Cascade_D_A_D.s2p")
Attenuator = Network("C:/Users/SH/PycharmProjects/Course_Python_Django/SP/Two_ports/Attenuator_9db.s2p")
F = S_75.f[:]

#----------------------------------------------------------
#Conversion and calculations
#----------------------------------------------------------

Cascade_t = rf.s2t(Cascade.s)
Attenuator_t = rf.s2t(Attenuator.s)

Matrix = np.zeros((len(Cascade_t), 2, 2), complex)
for i in range(len(Cascade_t)):

    Value_1 = Cascade_t[i]@Attenuator_t[i]
    Value_2 = linalg.sqrtm(Value_1)
    Value_3 = Value_2@linalg.inv(Attenuator_t[i])

    Matrix[i, 0, 0] = Value_3[0, 0]
    Matrix[i, 1, 0] = Value_3[1, 0]
    Matrix[i, 1, 1] = Value_3[1, 1]
    Matrix[i, 0, 1] = Value_3[0, 1]


Matrix_s = rf.t2s(Matrix)

#----------------------------------------------------------
#Plot
#----------------------------------------------------------
plt.figure()
plt.plot(F, 20*np.log10(S_75.s[:, 1-1, 1-1]), label='Measure', linewidth ='3')
plt.plot(F, 20*np.log10(Matrix_s[:,1-1,1-1]), label='Calc', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.legend()
plt.grid()

plt.figure()
plt.plot(F, 20*np.log10(  S_75.s[:,2-1, 1-1]), label='Measure', linewidth ='3')
plt.plot(F, 20*np.log10(Matrix_s[:,2-1, 1-1]), label='Calc', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.legend()
plt.grid()
plt.show()
#----------------------------------------------------------
#----------------------------------------------------------


