import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["rolling_av5"])
plt.title("згладжування ковзним середнім W = 5")
plt.show()