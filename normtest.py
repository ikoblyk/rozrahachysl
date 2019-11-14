from scipy.cluster.hierarchy import linkage
from sklearn import preprocessing
import numpy as np
from rozraha import hlp, data,x, y , sc_creator
import time as T
from pprint import pprint
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.cluster import KMeans
from scipy.spatial.distance import squareform, cdist
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist, squareform



e = dict()

rr = [sc_creator() for i in y]

r = [T.mktime(i.timetuple()) + i.microsecond / 1E61320517575 for i in x]

#e["x"] = r
#e["y"] = sc_creator()

#dd = pd.DataFrame(e)

h = hlp["mean"].to_numpy()
hh = h.transpose()
hlp_divided = pd.DataFrame()
a  = np.array([h])
b = np.array([hh])
result = h.flatten()
hlp_divided["one"] = h[:435]
hlp_divided["two"] = h[435:870]


ar = pdist(hlp_divided.to_numpy())
print("{}".format(ar))
Z = linkage(hlp_divided.to_numpy(), 'ward')
print("this is linkage{}".format(Z))



'''
plt.figure(figsize=(10, 7))
plt.title("Customer Dendograms")
dend = shc.dendrogram(Z)
plt.show()
'''
linked = linkage(hlp_divided.to_numpy(), 'single')

# calculate full dendrogram
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
shc.dendrogram(
    Z,
    leaf_rotation=90,  # rotates the x axis labels
    leaf_font_size=8,  # font size for the x axis labels
)
plt.show()



#print(hlp_divided["one"].to_numpy())
#print(squareform(hlp_divided["one"].to_numpy(),hlp_divided["two"] force='tomatrix'))

'''
print(squareform(hh, force='tomatrix'))

print(h)
print(cdist(h[0], ))
'''
#hlp_divided["one"] = h[:244]
#hlp_divided["two"] = h[244:487]
#hlp_divided["three"] = h[487:730]
#hlp_divided["four"] = h[730:973]

#plt.figure(figsize=(10, 7))
#plt.title("Customer Dendograms")
#dend = shc.dendrogram()

'''
cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='centroid')
print(cluster.fit_predict(hlp_divided.to_numpy()))
print(x.__len__())
'''

#print("this is distance matrix{}".format(pdist(hlp_divided[0].to_numpy()[:20])))

'''
plt.figure(figsize=(10, 7))
plt.scatter(x[:435], hlp_divided["one"], c=cluster.labels_, cmap='rainbow')
plt.show()
'''
'''

'''
'''
x_array = np.array(hlp['mean'])
normalized_X = preprocessing.normalize([x_array])
hlp["norm"] = normalized_X[0]


print(hlp)

r = [T.mktime(i.timetuple()) + i.microsecond / 1E61320517575 for i in x]

print("this is r {}".format(r))
e = dict()

rr = [sc_creator() for i in y]

e["x"] = r
e["y"] = sc_creator()

dd = pd.DataFrame(e)

kmeans = KMeans(n_clusters=25).fit(dd)
centroids = kmeans.cluster_centers_
print(centroids)
print(dd)
plt.scatter(dd["x"], dd["y"], c=kmeans.labels_.astype(float), s=50, alpha=0.5)

plt.show()
'''
