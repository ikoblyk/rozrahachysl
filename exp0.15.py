import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["exp0.15"])
plt.title("послідовне експоненціальне згладжування alpha = 0.15")
plt.show()