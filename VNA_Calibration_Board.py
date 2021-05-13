import skrf as rf
from skrf import Network
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

def Frequency_Range(fmin, fmax, Minimum_el_length,Maximum_el_length):
    dividerF = Maximum_el_length / Minimum_el_length
    N = 0
    i = 0
    F_sum = fmax
    F_val = fmax
    while N == 0:
        if F_sum > fmin:
            F_sum = F_sum / dividerF
            i = i + 1
        else:
            N = 1

    Value = i
    mas = np.zeros([Value+1, 1], float)

    N = 0
    i = Value-1
    while N == 0:
        if F_val > fmin:
            F_val = F_val / dividerF
            mas[i] = F_val
            i = i - 1
        else:
            N = 1
    mas[Value] = fmax
    return mas

def plot_Range(fmin, fmax, Minimum_el_length, Maximum_el_length):
    mas = Frequency_Range(fmin, fmax, Minimum_el_length, Maximum_el_length)
    dividerL = 360 / Maximum_el_length
    c = 3e8
    epsilon = 3
    for i in range(len(mas)-1):
        F = np.linspace(mas[i], mas[i+1], 100)
        EL = 360 * F / (mas[i+1] * dividerL)
        Length = (c/(mas[i+1]*sqrt(epsilon)*dividerL))*1000
        Text = f"{int(mas[i]):.0e}-{int(mas[i+1]):.0e} Гц"
        plt.plot(F/1e9, EL, label=f'L={float(Length):.2f} мм')
    plt.title('TRL Bands')
    plt.xlabel('F, ГГц')
    plt.ylabel('Электрическая длина')
    plt.grid()
    plt.legend()
    plt.show()


fmin = 2.5e9
fmax = 30e9

Minimum_el_length = 40
Maximum_el_length = 140

plot_Range(fmin,fmax, Minimum_el_length, Maximum_el_length)

'''
Frequency = np.linspace(fmin, fmax, N_Points)
El_length = 360*Frequency/(divider*fmax)
plt.plot(Frequency, El_length,    label='Эл длина')

'''














