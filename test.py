import matplotlib.pyplot as plt
import scipy as sc
from scipy.misc import derivative as der
import numpy as np
import math

def function(x):
    return pow(0.5, x)-0.1


epsilon1 = 1e-1
epsilon2 = 1e-2
epsilon3 = 1e-3
epsilon4 = 1e-4



def Lvl3b(x):
    return (math.exp(pow(x, -2))*10-math.sqrt(2*math.pi*x)-math.sin(x))

def Lvl3(x):
    return pow(x, 3)-3*pow(x, 2)-17*x+22


def Root_finder(a, b):
    x1 = a-Lvl3b(a)*((b-a)/(Lvl3b(b)-Lvl3b(a)))
    print(x1)
    if abs((x1-a)/(a))<=epsilon1:
        print(abs((x1-a)/(a)))
        return x1
    else:
        Root_finder(x1, b)
"""

if __name__ == '__main__':
    x2 = Root_finder(6, 1)
    x3 = Root_finder(x2, 1)
    x4 = Root_finder(x3, 1)
    x5 = Root_finder(x4, 1)
    x6 = Root_finder(x5, 1)
    x7 = Root_finder(x6, 1)
    print(x6)
"""


iterations=0

def Combined(a, b, epsilon, roundd):
    global iterations
    x1 = a - Lvl3b(a)/der(Lvl3b, a, 1)
    x2 = b-(a-b)/(Lvl3b(a)-Lvl3b(b))*Lvl3b(b)
    iterations+=1
    if abs(a-b)<=epsilon:
        print("eps = {}\t{}\t{}\t".format(epsilon, round(x2, roundd), iterations))
        return x2
    else:
        Combined(x1, x2, epsilon, roundd)


def Check(a, b, epsilon, roundd):
    global iterations
    iterations =0
    if Lvl3b(a)*der(Lvl3, a, 1.0)>0:
        return Combined(a, b, epsilon, roundd)
    else:
        return Combined(b, a, epsilon, roundd)



def Combined1(a, b, epsilon, roundd):
    global iterations
    x1 = a - Lvl3(a)/der(Lvl3, a, 1)
    x2 = b-(a-b)/(Lvl3(a)-Lvl3(b))*Lvl3(b)
    iterations+=1
    if abs(a-b)<=epsilon:
        print("eps = {}\t{}\t{}\t".format(epsilon, round(x2, roundd), iterations))
        return x2
    else:
        Combined1(x1, x2, epsilon, roundd)


def Check1(a, b, epsilon, roundd):
    global iterations
    iterations =0
    if Lvl3(a)*der(Lvl3, a, 1.0)>0:
        return Combined1(a, b, epsilon, roundd)
    else:
        return Combined1(b, a, epsilon, roundd)







print("Точність\t Значення кореня\t Кількість ітерацій")
Check(13, 15, 0.1, 1)
Check(13, 15, 0.01, 2)
Check(13, 15, 0.001, 3)
Check(13, 15, 0.0001, 4)

print("Рівень 1:")
print("Точність\t Значення кореня\t Кількість ітерацій")
Check1(13, 15, 0.1, 1)
Check1(13, 15, 0.01, 2)
Check1(13, 15, 0.001, 3)
Check1(13, 15, 0.0001, 4)


#Root_finder(15, 13)
#Root_finder(15, 13)

f2 = np.vectorize(Lvl3b)
result = np.arange(10, 20, 0.001)
plt.plot(result, f2(result))
plt.show()


