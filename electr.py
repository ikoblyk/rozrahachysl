import math, cmath
import matplotlib.pyplot as plt
import numpy as np


def plot_Ku_frequency(x, y):
    #sp= np.linspace(0, 22, 12)
    plt.plot(x, y)
    plt.show()




Rl = 7.3
Rg = 100

Rk = Rl+Rg

C = 0.01e-6

L = 12.3e-3

u1 = []

for i in range(12):
    u1.append(10)

f = [14.04, 13.31, 12.71, 11.89, 9.92, 8.53, 14.04, 14.92, 15.42, 16.14, 17.42, 20.78]

u2 = [5.8, 4.8, 3.8, 2.8, 1.8, 0.8, 5.8, 4.8, 3.8, 2.8, 1.8, 0.8]

Ku = [i/j for i, j in zip(u2, u1)]
print(u2[11]/u1[11])




resonanseHertz = 1/(2*math.pi*math.sqrt(L*C))
resonansewithoutwpi = 1/(math.sqrt(L*C))

ro = 1/(resonansewithoutwpi*C)

print("{}\t{}\t{}\t{}\t".format(resonansewithoutwpi*L, 1/(resonansewithoutwpi*C), L/(math.sqrt(L*C)), math.sqrt(L/C)))
print("Резонансна частота{}".format(resonanseHertz))

Q = ro/Rk
Q1 = resonansewithoutwpi*L/Rk

Kuc = [(1/1j*w*C)/(Rk+1j*(w*L-1/(w*C))) for w in f]
print(Kuc)
Kul =  [1j*w*C/(Rk+1j*(w*L-1/(w*C))) for w in f]
print(Kul)



print(Ku)


plot_Ku_frequency(f, Ku)