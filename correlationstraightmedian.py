from rozraha import hlp, turning_points
corr1m = hlp["mean"].corr(hlp["median_filter3"])
corr2m = hlp["mean"].corr(hlp["median_filter5"])
corr3m = hlp["mean"].corr(hlp["median_filter7"])
corr4m = hlp["mean"].corr(hlp["median_filter9"])
corr5m = hlp["mean"].corr(hlp["median_filter11"])
corr6m = hlp["mean"].corr(hlp["median_filter13"])
corr7m = hlp["mean"].corr(hlp["median_filter15"])


print("this is median corealtion не послідовне {}\n{}\n{}\n{}\n{}".format(corr1m, corr2m, corr3m, corr5m, corr7m))

n = hlp["median_filter3"].__len__()

turning_points3m = turning_points(hlp["median_filter3"],  n)
turning_points5m= turning_points(hlp["median_filter5"],  n)
turning_points7m = turning_points(hlp["median_filter7"],  n)
turning_points9m = turning_points(hlp["median_filter9"],  n)
turning_points11m = turning_points(hlp["median_filter11"],  n)
turning_points13m= turning_points(hlp["median_filter13"],  n)
turning_points15m= turning_points(hlp["median_filter15"],  n)


print("turning points median не послідовне:")
print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(turning_points3m, turning_points5m,turning_points7m,turning_points9m,turning_points11m,turning_points13m,turning_points15m))