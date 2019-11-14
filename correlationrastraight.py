from rozraha import hlp, turning_points

corr1_1 = hlp["mean"].corr(hlp["rolling_av3"])
corr2_1 = hlp["mean"].corr(hlp["rolling_av5"])
corr3_1 = hlp["mean"].corr(hlp["rolling_av7"])
corr4_1 = hlp["mean"].corr(hlp["rolling_av9"])
corr5_1 = hlp["mean"].corr(hlp["rolling_av11"])
corr6_1 = hlp["mean"].corr(hlp["rolling_av13"])
corr7_1 = hlp["mean"].corr(hlp["rolling_av15"])

print("correlation ковзне середнє не послідовне {}\n {}\n {}\n {}\n {} \n{} \n{}".format(corr1_1, corr2_1, corr3_1, corr4_1, corr5_1, corr6_1, corr7_1))

n = hlp["rolling_av3"].__len__()

turning_points3_1 = turning_points(hlp["rolling_av3"],  n)

turning_points5_1 = turning_points(hlp["rolling_av5"],  n)

turning_points7_1 = turning_points(hlp["rolling_av7"],  n)

turning_points9_1 = turning_points(hlp["rolling_av9"],  n)

turning_points11_1 = turning_points(hlp["rolling_av11"],  n)

turning_points13_1 = turning_points(hlp["rolling_av13"],  n)

turning_points15_1 = turning_points(hlp["rolling_av15"],  n)

print("turning points середнє ковзне не послідовне:")
print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(turning_points3_1, turning_points5_1,turning_points7_1,turning_points9_1,turning_points11_1,turning_points13_1,turning_points15_1))