import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["median_filter9"])
plt.title(" Медіанне згладжування W = 9")
plt.show()