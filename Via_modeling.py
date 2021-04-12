import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

SP_GL102 = Network('SP/Three_via_GL102.s6p')
SP_FR4   = Network('SP/Three_via_FR4.s6p')

plt.figure()
plt.title("GL102")
SP_GL102.plot_s_db(m=6-1, n=5-1, label='S65', linewidth ='3')
SP_GL102.plot_s_db(m=4-1, n=3-1, label='S43', linewidth ='3')
SP_GL102.plot_s_db(m=2-1, n=1-1, label='S21', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S , дБ')
plt.grid()
plt.figure()
plt.title("GL102")
SP_GL102.plot_s_smith(5-1,5-1, label='S55', linewidth ='3',draw_labels=True)
SP_GL102.plot_s_smith(3-1,3-1, label='S33', linewidth ='3',draw_labels=True)
SP_GL102.plot_s_smith(1-1,1-1, label='S11', linewidth ='3',draw_labels=True)

plt.figure()
plt.title("FR4")
SP_FR4.plot_s_db(m=6-1, n=5-1, label='S65', linewidth ='3')
SP_FR4.plot_s_db(m=4-1, n=3-1, label='S43', linewidth ='3')
SP_FR4.plot_s_db(m=2-1, n=1-1, label='S21', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S , дБ')
plt.grid()
plt.figure()
plt.title("FR4")
SP_FR4.plot_s_smith(5-1,5-1, label='S55', linewidth ='3',draw_labels=True)
SP_FR4.plot_s_smith(3-1,3-1, label='S33', linewidth ='3',draw_labels=True)
SP_FR4.plot_s_smith(1-1,1-1, label='S11', linewidth ='3',draw_labels=True)








plt.show()