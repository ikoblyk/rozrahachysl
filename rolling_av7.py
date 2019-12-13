import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["rolling_av7"])
plt.title("згладжування ковзним середнім W = 7")
plt.show()