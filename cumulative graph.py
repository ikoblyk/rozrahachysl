from rozraha import hlp
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))

mu = 200
sigma = 25
n_bins = 971


n, bins, patches = ax.hist(hlp["mean"], n_bins,  density=False, histtype='step', cumulative = 1,  label='Empirical')
plt.title("cumulative ")
plt.show()