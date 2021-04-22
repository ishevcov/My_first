import matplotlib.pyplot as plt
import skrf as rf
from skrf import Network

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

SP_GX_400 = Network('SP/VIA/GX13_400um.s2p')
SP_GX_800 = Network('SP/VIA/GX13_800um.s2p')
SP_GL_400 = Network('SP/VIA/GL102_400um.s2p')
SP_GL_800 = Network('SP/VIA/GL102_800um.s2p')


#S11 400
plt.figure()
plt.title("Core 400 мкм")
SP_GL_400.plot_s_db(m=1-1, n=1-1, label='GL102', linewidth ='3')
SP_GX_400.plot_s_db(m=1-1, n=1-1, label='GX13', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()

#S11 800
plt.figure()
plt.title("Core 800 мкм")
SP_GL_800.plot_s_db(m=1-1, n=1-1, label='GL102', linewidth ='3')
SP_GX_800.plot_s_db(m=1-1, n=1-1, label='GX13', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S11, дБ')
plt.grid()



#S21 400
plt.figure()
plt.title("Core 400 мкм")
SP_GL_400.plot_s_db(m=2-1, n=1-1, label='GL102', linewidth ='3')
SP_GX_400.plot_s_db(m=2-1, n=1-1, label='GX13', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()

#S21 800
plt.figure()
plt.title("Core 800 мкм")
SP_GL_800.plot_s_db(m=2-1, n=1-1, label='GL102', linewidth ='3')
SP_GX_800.plot_s_db(m=2-1, n=1-1, label='GX13 ', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, дБ')
plt.grid()



plt.show()