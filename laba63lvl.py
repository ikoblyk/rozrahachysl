import matplotlib.pyplot as plt
import scipy as sc


X = [2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9]
Y = [5.785, 5.685, 5.605, 5.545, 5.505, 5.480, 5.495, 5.510]


p2 = sc.polyfit(X, Y, 2)
p1 = sc.polyfit(X, Y, 1)
ypred1 = sc.polyval(p1, X)
ypred2 = sc.polyval(p2, X)

print("quadratic polynom: x1^(2)*{}+x2*{}+{}".format(p2[0], p2[1], p2[2]))
print("linear polynom: x*{}+{}".format(p1[0], p1[1]))



print("values predicted by linear polynom{}".format(ypred1))
print("values predicted by quadratic polynom{}".format(ypred2))


plt.scatter(X, Y)
plt.title("Рівень 3")
plt.plot(X, ypred2)
plt.plot(X, ypred1)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

