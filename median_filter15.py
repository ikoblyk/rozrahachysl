import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["median_filter15"])
plt.title(" Медіанне згладжування W = 15")
plt.show()