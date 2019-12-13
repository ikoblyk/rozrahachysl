import pandas as pd
import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["ra15from13"])
plt.title("послідовне згладжування ковзним середнім W = 15")
plt.show()