import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["median_filter3"])
plt.title(" Медіанне згладжування W = 3")
plt.show()