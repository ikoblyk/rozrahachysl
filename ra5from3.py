import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["ra5from3"])
plt.title("послідовне згладжування ковзним середнім W = 5")
plt.show()