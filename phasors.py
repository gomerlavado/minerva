import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

# Single phase system
v_rms= 220
i_rms = 1
v_max = math.sqrt(2) * v_rms
i_max = math.sqrt(2) * i_rms
theta_v = 60
theta_i = 30
omega = 2 * math.pi * 60
t = np.linspace(0, 0.1, 1000)

vt = v_max * np.cos(omega * t + math.radians(theta_v))
it = i_max * np.cos(omega * t + math.radians(theta_i))

plt.plot(t, vt, "r-", t, it, "b-", t, vt*it, "g-")
plt.hlines(220, 0, 0.1, colors="r", linestyles="dashed")
plt.show()

phi = theta_v - theta_i
p_avg = 0.5 * v_max * i_max * math.cos(math.radians(phi))
print(p_avg)

# Complex voltage, current and power
cv = complex(v_rms * math.cos(math.radians(theta_v)), v_rms * math.sin(math.radians(theta_v)))
ci = complex(i_rms * math.cos(math.radians(theta_i)), i_rms * math.sin(math.radians(theta_i)))

cp = cv*ci.conjugate()
print(cp)
print(cmath.polar(cp))

power_factor = math.cos(math.radians(phi))
