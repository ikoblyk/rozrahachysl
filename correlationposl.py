from rozraha import hlp, turning_points

corr1_1 = hlp["mean"].corr(hlp["ra5from3"])
corr3_1 = hlp["mean"].corr(hlp["ra7from5"])
corr4_1 = hlp["mean"].corr(hlp["ra9from7"])
corr5_1 = hlp["mean"].corr(hlp["ra11from"])
corr6_1 = hlp["mean"].corr(hlp["ra13from11"])
corr7_1 = hlp["mean"].corr(hlp["ra15from13"])

print("correlation ковзне середнє послідовне {}\n {}\n {}\n {}\n {} \n{}".format(corr1_1,  corr3_1, corr4_1, corr5_1, corr6_1, corr7_1))

n = hlp["rolling_av3"].__len__()

turning_points5 = turning_points(hlp["ra5from7"],  n)

turning_points7= turning_points(hlp["ra7from9"],  n)

turning_points9= turning_points(hlp["ra9from11"],  n)

turning_points11 = turning_points(hlp["ra11from13"],  n)

turning_points13 = turning_points(hlp["ra13from15"],  n)

turning_points15 = turning_points(hlp["ra15from13"],  n)

print("turning points послідовне середнд ковзне:")
print("{}\n{}\n{}\n{}\n{}\n{}".format(turning_points5, turning_points7,turning_points9,turning_points11,turning_points13,turning_points15))
