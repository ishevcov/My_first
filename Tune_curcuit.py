import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


F_CLK = 5e-6
V_REF = 1
DAC_Comp = 8
DAC_C = 4
DAC_R = 4

Number = 1
Razr = 3
Cap = 4e-12
Overlap = 0.2


def Cap_array(number, razr, cap, overlap):
    Value_Cap=0
    Cap_unity = (cap*(1+overlap))/(pow(2, razr)-1)
    for i in range(razr):
        Value_Cap = Value_Cap + pow(2, i)*float((number>>i)&0b1)*Cap_unity
    return Value_Cap




Matrix = np.zeros((pow(2, Razr), 2), float)
Input = [Number, Razr, Cap, Overlap]
for i in range(pow(2, Razr)):
    Matrix[i, 0] = i
    Matrix[i, 1] = Cap_array(i, Razr, 4e-12, 0.2)



plt.plot(Matrix[:, 0], Matrix[:, 1])
plt.grid()
plt.show()

print(Matrix)
print(Cap_array(*Input))



















