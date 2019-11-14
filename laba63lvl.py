import matplotlib.pyplot as plt
import scipy as sc
import math


X = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2]
Y = [1.924, 1.710, 1.525, 1.370, 1.264, 1.190, 1.148, 1.127]

p2 = sc.polyfit(X, Y, 2)
print(p2)
p1 = sc.polyfit(X, Y, 1)
ypred1 = sc.polyval(p1, X)
ypred2 = sc.polyval(p2, X)
print("real values {}".format(Y))
print("linear polynom values{}".format(ypred1))
print("Quadratic polynom values{}".format(ypred2))

print("quadratic polynom: x1^(2)*{}+x2*{}+{}".format(p2[0], p2[1], p2[2]))
print("linear polynom: x*{}+x*{}+{}".format(p2[0], p2[1], p2[2]))




plt.scatter(X, Y)
plt.plot(X, ypred2)
plt.plot(X, ypred1)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

