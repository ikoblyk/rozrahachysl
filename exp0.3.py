import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["exp0.3"])
plt.title("послідовне експоненціальне згладжування alpha = 0.3")
plt.show()