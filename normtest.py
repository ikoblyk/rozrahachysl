import numpy as np
from rozraha import hlp
from pprint import pprint
import pandas as pd
from objectproperty import object_prop


h = hlp["mean"].to_numpy()
hlp_divided = pd.DataFrame()

hlp_divided["one"] = h[:435]
hlp_divided["two"] = h[435:870]
tr = pd.DataFrame()
tr["three"] = h[870:]


aa = object_prop(hlp_divided["one"])
bb = object_prop(hlp_divided["two"])
cc = object_prop(tr["three"])


nw = np.vstack((aa.to_numpy(), bb.to_numpy(), cc.to_numpy()))

obj_p = pd.DataFrame(aa)

obj_p = obj_p.append(bb)

obj_p = obj_p.append(cc)

cols = obj_p.columns
