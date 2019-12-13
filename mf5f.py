import matplotlib.pyplot as plt
from rozraha import hlp, x

plt.plot(x, hlp["mf5f"])
plt.title(" Медіанне послідовне згладжування W = 5")
plt.show()