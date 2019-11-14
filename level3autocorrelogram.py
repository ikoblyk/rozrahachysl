from rozraha import hlp,data,  x
import matplotlib.pyplot as plt


#hlp = hlp.sort_values(by = "mean")
#print(hlp)

autocorfunc = list()

for i in range(1, 9):
    autocorfunc.append(hlp["mean"].autocorr(lag=i))




plt.bar(range(1, 9), autocorfunc)
plt.title("Корелограма автокореляційної функції")
plt.xlabel("Лаг")
plt.ylabel("Коефіцієнти кореляції")
plt.show()


