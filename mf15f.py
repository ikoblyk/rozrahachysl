import pandas as pd
import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["mf15f"])
plt.title(" Медіанне послідовне згладжування W = 15")
plt.show()