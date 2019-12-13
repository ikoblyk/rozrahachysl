import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["rolling_av9"])
plt.title("згладжування ковзним середнім W = 9")
plt.show()