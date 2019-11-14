from rozraha import hlp, turning_points, n

corr1_1m = hlp["mean"].corr(hlp["mf5f"])
corr2_1m = hlp["mean"].corr(hlp["mf7f"])
corr3_1m = hlp["mean"].corr(hlp["mf9f"])
corr5_1m = hlp["mean"].corr(hlp["mf11f"])
corr6_1m = hlp["mean"].corr(hlp["mf13f"])
corr7_1m = hlp["mean"].corr(hlp["mf15f"])


turning_points5m = turning_points(hlp["mf5f"],  n)
turning_points7m= turning_points(hlp["mf7f"],  n)
turning_points9m = turning_points(hlp["mf9f"],  n)
turning_points11m = turning_points(hlp["mf11f"],  n)
turning_points13m = turning_points(hlp["mf13f"],  n)
turning_points15m= turning_points(hlp["mf15f"],  n)


print("this is median corealtion (послідовне){}\n{}\n{}\n{}\n{}".format(corr1_1m, corr2_1m, corr3_1m, corr5_1m, corr7_1m))

print("turning points median poslidovne:")
print("{}\n{}\n{}\n{}\n{}\n{}".format(turning_points5m,turning_points7m,turning_points9m,turning_points11m,turning_points13m,turning_points15m))



