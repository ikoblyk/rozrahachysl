import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["exp0.25"])
plt.title("послідовне експоненціальне згладжування alpha = 0.25")
plt.show()