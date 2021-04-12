import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

SP_GL102 = Network('SP/Four_line_GL102.s16p')
SP_GX13  = Network("SP/Four_line_GX13.s16p")
F = SP_GL102.f[:]

#S11 GL102
plt.figure()
plt.title("GL102")
for x in 0,1,2,3:

    S11_GL102 = SP_GL102.s[:, (4 * x)+1-1, (4 * x)+1-1]
    S33_GL102 = SP_GL102.s[:, (4 * x)+3-1, (4 * x)+3-1]
    S13_GL102 = SP_GL102.s[:, (4 * x)+1-1, (4 * x)+3-1]
    S31_GL102 = SP_GL102.s[:, (4 * x)+3-1, (4 * x)+1-1]
    Sdd11 =20*np.log10((S11_GL102-S13_GL102-S31_GL102+S33_GL102)*0.5)

    if x == 0:
        Legend = "1mm"
    elif x == 1:
        Legend = "2mm"
    elif x ==2:
        Legend = "4mm"
    else:
        Legend = "8mm"

    plt.plot(F, Sdd11, label=Legend, linewidth ='3')
plt.grid()
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.legend()

#S11 GX13
plt.figure()
plt.title("GX13")
for x in 0,1,2,3:

    S11_GX13 = SP_GX13.s[:, (4 * x)+1-1, (4 * x)+1-1]
    S33_GX13 = SP_GX13.s[:, (4 * x)+3-1, (4 * x)+3-1]
    S13_GX13 = SP_GX13.s[:, (4 * x)+1-1, (4 * x)+3-1]
    S31_GX13 = SP_GX13.s[:, (4 * x)+3-1, (4 * x)+1-1]
    Sdd11 =20*np.log10((S11_GX13-S13_GX13-S31_GX13+S33_GX13)*0.5)

    if x == 0:
        Legend = "1mm"
    elif x == 1:
        Legend = "2mm"
    elif x ==2:
        Legend = "4mm"
    else:
        Legend = "8mm"

    plt.plot(F, Sdd11, label=Legend, linewidth ='3')
plt.grid()
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.legend()


#S21 GL102
plt.figure()
plt.title("GL102")
for x in 0, 1, 2, 3:

    S21_GL102 = SP_GL102.s[:, (4 * x) + 2 - 1, (4 * x) + 1 - 1]
    S41_GL102 = SP_GL102.s[:, (4 * x) + 4 - 1, (4 * x) + 1 - 1]
    S23_GL102 = SP_GL102.s[:, (4 * x) + 2 - 1, (4 * x) + 3 - 1]
    S43_GL102 = SP_GL102.s[:, (4 * x) + 4 - 1, (4 * x) + 3 - 1]
    Sdd21 = 20 * np.log10((S21_GL102 - S41_GL102 - S23_GL102 + S43_GL102) * 0.5)

    if x == 0:
        Legend = "1mm"
    elif x == 1:
        Legend = "2mm"
    elif x == 2:
        Legend = "4mm"
    else:
        Legend = "8mm"

    plt.plot(F, Sdd21, label=Legend, linewidth='3') #S21
plt.grid()
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.legend()

#S21 GX13
plt.figure()
plt.title("GX13")
for x in 0, 1, 2, 3:

    S21_GX13 = SP_GX13.s[:, (4 * x) + 2 - 1, (4 * x) + 1 - 1]
    S41_GX13 = SP_GX13.s[:, (4 * x) + 4 - 1, (4 * x) + 1 - 1]
    S23_GX13 = SP_GX13.s[:, (4 * x) + 2 - 1, (4 * x) + 3 - 1]
    S43_GX13 = SP_GX13.s[:, (4 * x) + 4 - 1, (4 * x) + 3 - 1]
    Sdd21 = 20 * np.log10((S21_GX13 - S41_GX13 - S23_GX13 + S43_GX13) * 0.5)

    if x == 0:
        Legend = "1mm"
    elif x == 1:
        Legend = "2mm"
    elif x == 2:
        Legend = "4mm"
    else:
        Legend = "8mm"

    plt.plot(F, Sdd21, label=Legend, linewidth='3') #S21
plt.grid()
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.legend()








plt.show()