import pandas as pd
import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["ra13from11"])
plt.title("послідовне згладжування ковзним середнім W = 13")
plt.show()