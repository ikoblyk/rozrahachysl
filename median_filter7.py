import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["median_filter7"])
plt.title(" Медіанне згладжування W = 7")
plt.show()