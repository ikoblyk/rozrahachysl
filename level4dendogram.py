from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import  numpy as np
from rozraha import hlp, x, data
from matplotlib import pyplot as plt
import pandas as pd
from pprint import pprint

hlp_divided = pd.DataFrame()
h = hlp["mean"].to_numpy()


#hlp_divided["one"] = h[:244]
#hlp_divided["two"] = h[244:487]
#hlp_divided["three"] = h[487:730]
#hlp_divided["four"] = h[730:973]

'''
S = 10
N = int(len(data)/S)
frames = [ data.iloc[i*S:(i+1)*S].copy() for i in range(N+1) ]
'''''
#df_by_duration = [i.groupby('duration') for i in data]

d = hlp.groupby("mean")

print(d["mean"].apply(pd.DataFrame.max))
print(hlp)


