import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["rolling_av3"])
plt.title("згладжування ковзним середнім W = 3")
plt.show()