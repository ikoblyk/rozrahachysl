import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["rolling_av15"])
plt.title("згладжування ковзним середнім W = 15")
plt.show()