from rozraha import hlp, x, data
import pandas as pd

hlp_divided = pd.DataFrame()
h = hlp["mean"].to_numpy()



hlp_divided["one"] = h[:324]
hlp_divided["two"] = h[324:648]
hlp_divided["three"] = h[648:972]

print(hlp["mean"].corr())



print("Frame after division by 3 \n{}".format(hlp_divided))
print("CORRELATION MATRIX\n{}".format(hlp_divided.corr()))



