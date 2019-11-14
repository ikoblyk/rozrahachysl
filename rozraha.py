import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as DT
from datetime import timedelta
import time as T
import numpy as np
import math
from pandas.plotting import register_matplotlib_converters
from  scipy.stats import t, sem
from scipy.signal import medfilt
from sklearn.metrics import r2_score
from sklearn.cluster import KMeans
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist
from scipy.cluster import hierarchy
from pprint import  pprint


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
print(data)

data.dropna(inplace=True)
data.drop_duplicates(inplace=True)


time = [str(d) for d in data['duration']]
dates = [str(dt).split()[0] for dt in data['date']]
print(time[23])
print(dates[12])
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
sum = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].sum()))
print("sum")
print(sum)
mean = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].mean()))
print("mean")
print(mean)
max = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].max()))
print("max")
print(max)
min = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].min()))
print("min")
print(min)
median = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].median()))
print("meadian")
print(median)
mode = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].mode()))
print("mode")
print(mode)
count = T.strftime('%H:%M:%S', T.gmtime(hlp['mean'].count()))
print("count")
print(count)
skrew = hlp['mean'].skew()
print("skrew")
print(skrew)
kurt = hlp['mean'].kurt()
print("kurt")
print(kurt)
stdev = hlp['mean'].std()
print("standart deviation")
print(stdev)
stderr = stdev/math.sqrt(hlp.__len__())
print("standart error")
print(stderr)
print("sample variance")
print("{}".format(hlp["mean"].var()))



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

corr1 = hlp["mean"].corr(hlp["rolling_av3"])
corr2 = hlp["mean"].corr(hlp["ra5from3"])
corr3 = hlp["mean"].corr(hlp["ra7from5"])
corr4 = hlp["mean"].corr(hlp["ra9from7"])
corr5 = hlp["mean"].corr(hlp["ra11from9"])
corr6 = hlp["mean"].corr(hlp["ra13from11"])
corr7 = hlp["mean"].corr(hlp["ra15from13"])

corr1_1 = hlp["mean"].corr(hlp["rolling_av3"])
corr2_1 = hlp["mean"].corr(hlp["rolling_av5"])
corr3_1 = hlp["mean"].corr(hlp["rolling_av7"])
corr4_1 = hlp["mean"].corr(hlp["rolling_av9"])
corr5_1 = hlp["mean"].corr(hlp["rolling_av11"])
corr6_1 = hlp["mean"].corr(hlp["rolling_av13"])
corr7_1 = hlp["mean"].corr(hlp["rolling_av15"])

print("correlation \n{} \n{} \n{} \n{} \n{}\n {}\n {}".format(corr1, corr2, corr3, corr4, corr5, corr6, corr7))


print("correlation послідовне {}\n {}\n {}\n {}\n {} \n{} \n{}".format(corr1_1, corr2_1, corr3_1, corr4_1, corr5_1, corr6_1, corr7_1))

n = hlp["rolling_av3"].__len__()

turning_points3_1 = turning_points(hlp["rolling_av3"],  n)

turning_points5_1 = turning_points(hlp["rolling_av5"],  n)

turning_points7_1 = turning_points(hlp["rolling_av7"],  n)

turning_points9_1 = turning_points(hlp["rolling_av9"],  n)

turning_points11_1 = turning_points(hlp["rolling_av11"],  n)

turning_points13_1 = turning_points(hlp["rolling_av13"],  n)

turning_points15_1 = turning_points(hlp["rolling_av15"],  n)

turning_points5 = turning_points(hlp["ra5from3"],  n)
turning_points3 = turning_points(hlp["rolling_av3"],  n)
turning_points7 = turning_points(hlp["ra7from5"],  n)
turning_points9 = turning_points(hlp["ra9from7"],  n)
turning_points11 = turning_points(hlp["ra11from9"],  n)
turning_points13 = turning_points(hlp["ra13from11"],  n)
turning_points15 = turning_points(hlp["ra15from13"],  n)

print("turning points:")
print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(turning_points3_1, turning_points5_1,turning_points7_1,turning_points9_1,turning_points11_1,turning_points13_1,turning_points15_1))

print("turning points: (послідовне)")
print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(turning_points3, turning_points9,turning_points15,turning_points13,turning_points11,turning_points5,turning_points7))


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




corr1m = hlp["mean"].corr(hlp["median_filter3"])
corr2m = hlp["mean"].corr(hlp["median_filter5"])
corr3m = hlp["mean"].corr(hlp["median_filter7"])
corr4m = hlp["mean"].corr(hlp["median_filter9"])
corr5m = hlp["mean"].corr(hlp["median_filter11"])
corr6m = hlp["mean"].corr(hlp["median_filter13"])
corr7m = hlp["mean"].corr(hlp["median_filter15"])

corr1_1m = hlp["mean"].corr(hlp["mf5f"])
corr2_1m = hlp["mean"].corr(hlp["mf7f"])
corr3_1m = hlp["mean"].corr(hlp["mf9f"])
corr5_1m = hlp["mean"].corr(hlp["mf11f"])
corr6_1m = hlp["mean"].corr(hlp["mf13f"])
corr7_1m = hlp["mean"].corr(hlp["mf15f"])


print("this is median corealtion (послідовне){}\n{}\n{}\n{}\n{}".format(corr1_1m, corr2_1m, corr3_1m, corr5_1m, corr7_1m))

print("this is median corealtion {}\n{}\n{}\n{}\n{}".format(corr1m, corr2m, corr3m, corr5m, corr7m))


turning_points5m = turning_points(hlp["mf5f"],  n)
turning_points7m= turning_points(hlp["mf7f"],  n)
turning_points9m = turning_points(hlp["mf9f"],  n)
turning_points11m = turning_points(hlp["mf11f"],  n)
turning_points13m = turning_points(hlp["mf13f"],  n)
turning_points15m= turning_points(hlp["mf15f"],  n)


print("turning points median :")
print("{}\n{}\n{}\n{}\n{}\n{}".format(turning_points9m,turning_points15m,turning_points13m,turning_points11m,turning_points5m,turning_points7m))


alpha_l = [0.1, 0.15, 0.2, 0.25, 0.3]

for i in alpha_l:
    hlp["exponentialra{}".format(i)] = hlp["mean"].ewm(alpha=i).mean()

hlp["exp0.1"] = hlp["mean"].ewm(alpha = 0.1).mean()

for i in range(1, 5):
    hlp["exp{}".format(alpha_l[i])] = hlp["mean"].ewm(alpha=alpha_l[i-1]).mean()

print("exp check{}".format(hlp["exponentialra0.15"][87]))
corr01 = hlp["mean"].corr(hlp["exponentialra0.1"])

corr15 = hlp["mean"].corr(hlp["exponentialra0.15"])

corr02 = hlp["mean"].corr(hlp["exponentialra0.2"])

corr025= hlp["mean"].corr(hlp["exponentialra0.25"])

corr03 =hlp["mean"].corr(hlp["exponentialra0.3"])
print("correaltion exp 1")

print("{}\n{}\n{}\n{}\n{}".format(corr01, corr15, corr02, corr025, corr03))


corr011 = hlp["mean"].corr(hlp["exp0.1"])

corr155 = hlp["mean"].corr(hlp["exp0.15"])

corr022 = hlp["mean"].corr(hlp["exp0.2"])

corr0255= hlp["mean"].corr(hlp["exp0.25"])

corr033 =hlp["mean"].corr(hlp["exp0.3"])

print("correaltion exp 2")

print("{}\n{}\n{}\n{}\n{}".format(corr011, corr155, corr022, corr0255, corr033))


turning_pointexp1 = turning_points(hlp["exponentialra0.1"],  n)

turning_pointsexp15= turning_points(hlp["exponentialra0.15"],  n)

turning_pointexp2_ = turning_points(hlp["exponentialra0.2"],  n)

turning_pointexp25= turning_points(hlp["exponentialra0.25"],  n)

turning_pointexp3 = turning_points(hlp["exponentialra0.3"],  n)


turning_pointexp1aft = turning_points(hlp["exp0.1"],  n)
turning_pointexp15aft = turning_points(hlp["exp0.15"],  n)
turning_pointexp2aft = turning_points(hlp["exp0.2"],  n)
turning_pointexp25aft = turning_points(hlp["exp0.25"],  n)
turning_pointexp3aft = turning_points(hlp["exp0.3"],  n)


print("exp {}\t{}\t{}\t{}\t{}".format(turning_pointexp1, turning_pointsexp15,turning_pointexp2_,turning_pointexp25,turning_pointexp3,))
print("exp 2{}\t{}\t{}\t{}\t{}".format(turning_pointexp1aft, turning_pointexp15aft,turning_pointexp2aft,turning_pointexp25aft,turning_pointexp3aft))
print("е дата{}".format(dates[0]))




r = [T.mktime(i.timetuple()) + i.microsecond / 1E61320517575 for i in x]

print("this is r {}".format(r))
e = dict()

rr = [sc_creator() for i in y]

e["x"] = r
e["y"] = sc_creator()

dd = pd.DataFrame(e)

''''
kmeans = KMeans(n_clusters=4).fit(dd)
centroids = kmeans.cluster_centers_
print(centroids)
print(dd)

S = 10
N = int(len(data)/S)
frames = [ data.iloc[i*S:(i+1)*S].copy() for i in range(N+1) ]

df_by_duration = [i.groupby('duration') for i in frames]


for i in df_by_duration:
    pprint(i.describe().head())

print(hlp)

'''


'''
plt.scatter(dd["x"], dd["y"], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()



plt.plot(x, y)
plt.show()




'''



'''
corr3 =

corr5 =

corr7 =

corr9 =

corr11 =

corr13 =

corr15 =


ax.plot(hlp["ra7from5"])
ax.plot(hlp["ra9from7"])
ax.plot(hlp["ra11from9"])
ax.plot(hlp["ra13from11"])


ax.plot(x, hlp["median_filter15"], color = "green")
plt.title("real ")


plt.show()



'''



confidence = 0.95


n = hlp.__len__()
h = stderr* t.ppf((1 + confidence) / 2, n - 1)

start = hlp["mean"].mean() - h

end = hlp["mean"].mean() + h


print("{} \t {}".format(start, end))
np.random.seed(19680801)

mu = 200
sigma = 25
n_bins = 971


print(hlp.corr(method="pearson"))

print(hlp["mean"].autocorr())






#ax.hist(hlp["mean"], bins=50, density=True, cumulative=-1)

#ax.plot(x, hlp["mf15f"])


#plt.show()






'''

fig, ax = plt.subplots(figsize=(8, 4))


n, bins, patches = ax.hist(hlp["mean"], n_bins,  density=False, histtype='step', cumulative = 1,  label='Empirical')



yy = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
yy = yy.cumsum()
yy /= yy[-1]


ax.plot(bins, yy, 'k--', linewidth=1.5, label='Theoretical')

plt.show()


ax.hist(hlp["mean"], bins=bins, density=True, histtype='step', cumulative=1)


ax.grid(True)
ax.legend(loc='right')
ax.set_title('Cumulative diagram')
ax.set_xlabel('time')

plt.show()










#ax.hist(data['duration'], bins=bins, density=True, histtype='step', cumulative=-1,
     #   label='Reversed emp.') 362, in <module>
    plt.scatter(dd[x], dd[y], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
  File "/usr/local/lib/python3.6/dist-packages/pandas/core/frame.py", line 3001, in _

ax.grid(True)
ax.legend(loc='right')
ax.set_title('Cumulative step histograms')
ax.set_xlabel('Annual rainfall (mm)')
ax.set_ylabel('Likelihood of occurrence')

plt.show()

n_bins = 100


fig, ax = plt.subplots(figsize=(8, 4))
n, bins, patches = ax.hist([l for l in data['duration']], n_bins, density=True, histtype='step',cumulative=True, label='Empirical')



#ax.hist([l for l in data['duration']],  bins = bins,density = True,  cumulative = -1)
#ax2.hist([l for l in data['duration']],5, cumulative = True)
plt.show()




y1 = [y[i]for i in range(0, 360)]

fig = plt.figure()
ax = fig.add_subplot(111, polar = True)
time2 = [timedelta(seconds=np.pi*2 * t.second).seconds for t in x]
theta = np.arange(0., 2., 1./180.)*np.pi
plt.plot(theta, y1)
plt.xlabel('Date')
plt.ylabel('Time')
plt.title('Peak Time')
ticks =[str(x[i]) for i in range(0,900,60 )]
ax.set_xticks(ticks)
'''


'''
print(dates[1])

f, (ax1, ax2) = plt.subplots(1, 2,sharex=True)
ax1.plot_date(data['Індекс дня'], data['average'], linestyle = "solid", color = "black" , marker = "")
plt.plot_date(data['date'], data['duration'], linestyle = "solid", color = "red", marker = "" )
plt.gcf().autofmt_xdate()
f
'''

