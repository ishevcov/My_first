import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

SP = Network('C:/Users/SH/Desktop/homework_V2/Рабочий стол/Утюг/Микрополосковая линия/S2P/Four_line_Solaris.s8p')


plt.figure()

SP.plot_s_db(m=2-1,    n=1-1, label='S21', linewidth ='3')
SP.plot_s_db(m=4-1,    n=3-1, label='S43', linewidth ='3')
SP.plot_s_db(m=6-1,    n=5-1, label='S65', linewidth ='3')
SP.plot_s_db(m=8-1,    n=7-1, label='S87', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('SP, дБ')
plt.grid()

plt.figure()

SP.plot_s_db(m=1-1,    n=1-1, label='S11', linewidth ='3')
SP.plot_s_db(m=3-1,    n=3-1, label='S33', linewidth ='3')
SP.plot_s_db(m=5-1,    n=5-1, label='S55', linewidth ='3')
SP.plot_s_db(m=7-1,    n=7-1, label='S77', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('SP, дБ')
plt.grid()


plt.show()

