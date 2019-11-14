import matplotlib.pyplot as plt
from rozraha import hlp
from pandas.plotting import autocorrelation_plot

autocorrelation_plot(hlp["mean"])
plt.title("Графік автокореляційної функції")
plt.show()