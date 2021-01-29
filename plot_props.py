import numpy as np
import matplotlib.pyplot as plt
import xsteam2

temp_range = np.linspace(300, 647.096+10, 100)
s_vap = np.array([xsteam2.sV_T(i) for i in temp_range])
s_liq = np.array([xsteam2.sL_T(i) for i in temp_range])
s_press = []
for p in (0.1, 0.5, 1.0, 1.5, 3.0, 6.0, 9.0, 15.0):
    s_press.append(np.array([xsteam2.s_pT(p, t) for t in temp_range]))

plt.plot(s_vap, temp_range)
plt.plot(s_liq, temp_range)
for pdata in s_press:
    plt.plot(pdata, temp_range)

plt.show()

