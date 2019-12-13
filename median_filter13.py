import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["median_filter13"])
plt.title(" Медіанне згладжування W = 13")
plt.show()