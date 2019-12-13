import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["median_filter11"])
plt.title(" Медіанне згладжування W = 11")
plt.show()