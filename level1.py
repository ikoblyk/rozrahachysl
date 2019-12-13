import matplotlib.pyplot as plt
from rozraha import x, y, hlp, data
import time as T
import math

print(data)

fstlevel = dict()

fstlevel["sum"] = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].sum()))

fstlevel["mean"] = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].mean()))

fstlevel["max"] = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].max()))

fstlevel["min"] = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].min()))

fstlevel["median"] = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].median()))

fstlevel["mode"] = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].mode()))

fstlevel["count"] = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].count()))

fstlevel["skrew"] = hlp['mean'].skew()

fstlevel["kurt"] = hlp['mean'].kurt()

fstlevel["standart deviation"] = hlp['mean'].std()

fstlevel["standart error"] = fstlevel["standart deviation"]/math.sqrt(hlp.__len__())

fstlevel["sample variation"] = hlp["mean"].var()

print(fstlevel)

plt.plot(x, y)
plt.title("Вхідні дані")
plt.show()