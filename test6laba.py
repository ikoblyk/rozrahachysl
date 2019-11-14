import pandas as pd
import matplotlib.pyplot as plt
import scipy as sc
import numpy as np
import math
from scipy.signal import remez

data = pd.DataFrame()
data["Господарство"] = list()
l = ["ім. Ю. Федьковича",
"Заповіт Т. Шевченка",
"ім. В. Чорновола",
"Чумацький шлях",
"ім. Лесі Українки",
"Україна",
"Буковина",
"ім. Т. Шевченка",
"ім. М. Вовчка",
"Карпати",
"ім. Стуса",
"ім. Г. Сковороди",
"ім. Щорса",
"ім. 0. Кобилянської",
"Дружба",
"ім. 1-го Вересня",
"ім. Івана Франка",
"Нове життя",
"ім. Я. Галана"
]
data["Господарство"] = l


x1 = []
x2 = []
x3 = []

for i in range(19):
    x1.append(sc.random.uniform(21.6, 42.2))
    x2.append(sc.random.uniform(40, 63))
    x3.append(sc.random.uniform(209, 534.5))

data["x0"] = x1
data["x1"] = x2
data["x2"] = x3
print(data)

coef  = [-0.23059385, -0.03694656]

inters  = 55.90475011534866
def function(k, x):
    return 23.5*k*math.exp(0.34*k*x)+math.sqrt(1.4*k)


def vidr(k):
    return 0.2, 5.4+k


X = np.arange(-10,20, 0.05)
Y = [function(2, i) for i in X]

n = remez(2, X*2, Y)
print(n)
print(Y)
plt.plot(X,Y)
plt.show()


