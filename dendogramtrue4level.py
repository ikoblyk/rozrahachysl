from scipy.cluster.hierarchy import linkage
from sklearn import preprocessing

import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc

from scipy.spatial.distance import pdist, squareform
from normtest import  nw


min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(nw)
print("після нормування {}".format(x_scaled))

Y = pdist(x_scaled, 'euclidean')
print("Матриця близькостей{}".format(squareform(Y)))

Z = linkage(x_scaled, 'single')
plt.figure(figsize=(25, 10))
plt.title('Дендограма')
plt.xlabel('індекс')
plt.ylabel('відстань')
shc.dendrogram(
    Z,
    truncate_mode='lastp',
    p=10,


)
plt.show()



