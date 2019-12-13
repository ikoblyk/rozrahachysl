import pandas as pd

from datetime import datetime as DT

import time as T

import math
from pandas.plotting import register_matplotlib_converters

from scipy.signal import medfilt


register_matplotlib_converters()



def converter_to_datetime(seconds):
    minutes = hours = None
    if seconds<60:
        hours = 0
        minutes = 0
        seconds = seconds
    elif 60 <= seconds < 3600:
        minutes = math.floor(seconds/60)
        seconds-=minutes*60
        hours = 0
    elif seconds>=3600:
        hours = math.floor(seconds/3600)
        seconds-=hours*3600
        minutes = math.floor(seconds/60)
        seconds-=minutes*60
    else:
        seconds = minutes = hours = 0
    st = "{}:{}:{}".format(int(hours), int(minutes), int(seconds))
    d = DT.strptime(st, '%H:%M:%S').time()
    return d




data = pd.read_excel(r'/home/ivan/Documents/V6.xls')


data.dropna(inplace=True)
data.drop_duplicates(inplace=True)


time = [str(d) for d in data['duration']]
dates = [str(dt).split()[0] for dt in data['date']]

x = [DT.strptime(date, "%Y-%m-%d") for date in dates]
y = [DT.strptime(t, "%H:%M:%S").time() for t in time]


def sc_creator():
    scs = []
    for i in range(0, 973):
        sum = 0
        a = time[i].split(":")
        sum+= 3600*float(a[0])+60*float(a[1])+float(a[2])
        scs.append(sum)
    return scs




def turning_points(frame, size):
    turning_points = 0
    for i in range( 1, size-2):
        if (frame[i]<frame[i+1] and frame[i+1]>frame[i+2]) or ( frame[i]>frame[i+1] and frame[i+1]<frame[i+2]):
            turning_points+=1
    return turning_points


hlp = pd.DataFrame(columns = ['mean', 'median'])
hlp['mean'] = sc_creator()



hlp["rolling_av5"] = hlp["mean"].rolling(5, min_periods=1).mean()


hlp["rolling_av3"] = hlp["mean"].rolling(3, min_periods=1).mean()


hlp["rolling_av7"] = hlp["mean"].rolling(7, min_periods=1).mean()

hlp["rolling_av9"] = hlp["mean"].rolling(9, min_periods=1).mean()


hlp["rolling_av11"] = hlp["mean"].rolling(11, min_periods=1).mean()
hlp["rolling_av13"] = hlp["mean"].rolling(13, min_periods=1).mean()


hlp["rolling_av15"] = hlp["mean"].rolling(15, min_periods=1).mean()


#fig, ax = plt.subplots(figsize=(8, 4))

hlp["ra5from3"] = hlp["rolling_av3"].rolling(5, min_periods=1).mean()
hlp["ra7from5"] = hlp["ra5from3"].rolling(window=7, min_periods=1).mean()
hlp["ra9from7"] = hlp["ra7from5"].rolling(window=9, min_periods=1).mean()
hlp["ra11from9"] = hlp["ra9from7"].rolling(window=11, min_periods=1).mean()
hlp["ra13from11"] = hlp["ra11from9"].rolling(window=13, min_periods=1).mean()
hlp["ra15from13"] = hlp["ra13from11"].rolling(window=15, min_periods=1).mean()



n = hlp["rolling_av3"].__len__()

hlp["median_filter3"] = medfilt(hlp["mean"])
hlp["median_filter5"]= medfilt(hlp["mean"], 5)
hlp["median_filter7"] = medfilt(hlp["mean"], 7)
hlp["median_filter9"] = medfilt(hlp["mean"], 9)
hlp["median_filter11"] = medfilt(hlp["mean"], 11)
hlp["median_filter13"] = medfilt(hlp["mean"], 13)
hlp["median_filter15"] = medfilt(hlp["mean"], 15)


hlp["mf5f"]= medfilt(hlp["mean"], 5)
hlp["mf7f"] = medfilt(hlp["mf5f"], 7)
hlp["mf9f"] = medfilt(hlp["mf7f"], 9)
hlp["mf11f"] = medfilt(hlp["mf9f"], 11)
hlp["mf13f"] = medfilt(hlp["mf11f"], 13)
hlp["mf15f"] = medfilt(hlp["mf13f"], 15)

alpha_l = [0.1, 0.15, 0.2, 0.25, 0.3]

for i in alpha_l:
    hlp["exponentialra{}".format(i)] = hlp["mean"].ewm(alpha=i).mean()

hlp["exp0.1"] = hlp["mean"].ewm(alpha = 0.1).mean()
hlp["exp0.15"] = hlp["exponentialra0.1"].ewm(alpha = 0.15).mean()
hlp["exp0.2"] = hlp["exp0.15"].ewm(alpha = 0.2).mean()
hlp["exp0.25"] = hlp["exp0.2"].ewm(alpha = 0.25).mean()
hlp["exp0.3"] = hlp["exp0.25"].ewm(alpha = 0.3).mean()







r = [T.mktime(i.timetuple()) + i.microsecond / 1E61320517575 for i in x]

e = dict()

rr = [sc_creator() for i in y]

e["x"] = r
e["y"] = sc_creator()

dd = pd.DataFrame(e)






