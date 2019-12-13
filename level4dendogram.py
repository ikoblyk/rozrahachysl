from scipy.cluster.hierarchy import dendrogram, linkage
from rozraha import hlp
from matplotlib import pyplot as plt
import pandas as pd
import scipy.spatial.distance as ssd
from sklearn import preprocessing
from normtest import nw, obj_p
from pprint import pprint

pprint(obj_p)



hlp_divided = pd.DataFrame()
h = hlp["mean"].to_numpy()

d = preprocessing.normalize(nw)

print("normalized{}".format(d))

dd = ssd.pdist(d)

matr = ssd.squareform(dd)

print("distance matrix{}".format(matr))

Z = linkage(d, 'single')
plt.figure(figsize=(25, 10))
plt.title("Дендограма")
dendrogram(
    Z,
    truncate_mode='lastp',
    p =10,


)
plt.show()







