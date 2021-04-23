import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network
import numpy as np


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

def S_D(P1, P3, P2, P4, Type, Folder_1, Title_1, Legend_1):
    SP = Network(Folder_1)
    F = SP.f[:]
    P1 -= 1
    P2 -= 1
    P3 -= 1
    P4 -= 1
    if int(Type) == 11:
        SDD = 0.5*(SP.s[:, P1, P1]-SP.s[:, P1, P3]-SP.s[:, P3, P1]+SP.s[:, P3, P3])
    elif int(Type) == 21:
        SDD = 0.5*(SP.s[:, P2, P1]-SP.s[:, P4, P1]-SP.s[:, P2, P3]+SP.s[:, P4, P3])

    plt.title(Title_1)
    plt.plot(F, 20*np.log10(SDD), label=Legend_1, linewidth ='3')
    plt.xlabel('F, Гц')
    plt.ylabel(f'S{Type}, дБ')


Title   = "Core 400 мкм"
Folder_1   = "SP/VIA/GL102_400um_diff_35.s4p"
Legend_1   = "GL102"

Folder_2   = "SP/VIA/GX13_400um_diff_35.s4p"
Legend_2   = "GX13"


plt.figure()
S_D(1, 2, 3, 4, 21, Folder_1, Title, Legend_1)
S_D(1, 2, 3, 4, 21, Folder_2, Title, Legend_2)
plt.legend()
plt.grid()


plt.figure()
S_D(1, 2, 3, 4, 11, Folder_1, Title, Legend_1)
S_D(1, 2, 3, 4, 11, Folder_2, Title, Legend_2)
plt.legend()
plt.grid()
plt.show()

#