import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network
import numpy as np
import math, cmath


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

SP_input_50  = Network("SP/Test_diff/S11_input_50.s2p")
SP_input_100 = Network("SP/Test_diff/S11_input_100.s2p")
SP_input_200 = Network("SP/Test_diff/S11_input_200.s2p")
SP_input_400 = Network("SP/Test_diff/S11_input_400.s2p")

SP_load_50  = Network("SP/Test_diff/S11_load_50.s2p")
SP_load_100 = Network("SP/Test_diff/S11_load_100.s2p")
SP_load_200 = Network("SP/Test_diff/S11_load_200.s2p")
SP_load_400 = Network("SP/Test_diff/S11_load_400.s2p")

Sdd11_load_50  = 0.5*(SP_load_50.s[:, 1-1, 1-1]+SP_load_50.s[:, 2-1, 2-1])
Sdd11_load_100 = 0.5*(SP_load_100.s[:, 1-1, 1-1]+SP_load_100.s[:, 2-1, 2-1])
Sdd11_load_200 = 0.5*(SP_load_200.s[:, 1-1, 1-1]+SP_load_200.s[:, 2-1, 2-1])
Sdd11_load_400 = 0.5*(SP_load_400.s[:, 1-1, 1-1]+SP_load_400.s[:, 2-1, 2-1])

Sdd11_input_50   = 0.5*(SP_input_50.s[:, 1-1, 1-1]-SP_input_50.s[:, 1-1, 2-1]-SP_input_50.s[:, 2-1, 1-1]+SP_input_50.s[:, 2-1, 2-1])
Sdd11_input_100  = 0.5*(SP_input_100.s[:, 1-1, 1-1]-SP_input_100.s[:, 1-1, 2-1]-SP_input_100.s[:, 2-1, 1-1]+SP_input_100.s[:, 2-1, 2-1])
Sdd11_input_200  = 0.5*(SP_input_200.s[:, 1-1, 1-1]-SP_input_200.s[:, 1-1, 2-1]-SP_input_200.s[:, 2-1, 1-1]+SP_input_200.s[:, 2-1, 2-1])
Sdd11_input_400  = 0.5*(SP_input_400.s[:, 1-1, 1-1]-SP_input_400.s[:, 1-1, 2-1]-SP_input_400.s[:, 2-1, 1-1]+SP_input_400.s[:, 2-1, 2-1])

F = SP_input_50.f[:]




with open("SP/Test_diff/Results/S11_input_50.s4p", "w") as file:
    file.write("# Hz	S	RI	R	50.000000 \n")
    for i in range(0, len(F)):
        file.write(f"{F[i]} {Sdd11_input_50[i].real} {Sdd11_input_50[i].imag} \n")

with open("SP/Test_diff/Results/S11_input_100.s4p", "w") as file:
    file.write("# Hz	S	RI	R	50.000000 \n")
    for i in range(0, len(F)):
        file.write(f"{F[i]} {Sdd11_input_100[i].real} {Sdd11_input_100[i].imag} \n")

with open("SP/Test_diff/Results/S11_input_200.s4p", "w") as file:
    file.write("# Hz	S	RI	R	50.000000 \n")
    for i in range(0, len(F)):
        file.write(f"{F[i]} {Sdd11_input_200[i].real} {Sdd11_input_200[i].imag} \n")

with open("SP/Test_diff/Results/S11_input_400.s4p", "w") as file:
    file.write("# Hz	S	RI	R	50.000000 \n")
    for i in range(0, len(F)):
        file.write(f"{F[i]} {Sdd11_input_400[i].real} {Sdd11_input_400[i].imag} \n")

#------

with open("SP/Test_diff/Results/S11_load_50.s4p", "w") as file:
    file.write("# Hz	S	RI	R	50.000000 \n")
    for i in range(0, len(F)):
        file.write(f"{F[i]} {Sdd11_load_50[i].real} {Sdd11_load_50[i].imag} \n")

with open("SP/Test_diff/Results/S11_load_100.s4p", "w") as file:
    file.write("# Hz	S	RI	R	50.000000 \n")
    for i in range(0, len(F)):
        file.write(f"{F[i]} {Sdd11_load_100[i].real} {Sdd11_load_100[i].imag} \n")

with open("SP/Test_diff/Results/S11_load_200.s4p", "w") as file:
    file.write("# Hz	S	RI	R	50.000000 \n")
    for i in range(0, len(F)):
        file.write(f"{F[i]} {Sdd11_load_200[i].real} {Sdd11_load_200[i].imag} \n")

with open("SP/Test_diff/Results/S11_load_400.s4p", "w") as file:
    file.write("# Hz	S	RI	R	50.000000 \n")
    for i in range(0, len(F)):
        file.write(f"{F[i]} {Sdd11_load_400[i].real} {Sdd11_load_400[i].imag} \n")










file.close()
