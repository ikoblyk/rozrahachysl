import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["rolling_av11"])
plt.title("згладжування ковзним середнім W = 11")
plt.show()