import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["median_filter5"])
plt.title(" Медіанне згладжування W = 5")
plt.show()