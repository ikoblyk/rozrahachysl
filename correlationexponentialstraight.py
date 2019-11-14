from rozraha import hlp, turning_points, n

corr01 = hlp["mean"].corr(hlp["exponentialra0.1"])

corr15 = hlp["mean"].corr(hlp["exponentialra0.15"])

corr02 = hlp["mean"].corr(hlp["exponentialra0.2"])

corr025= hlp["mean"].corr(hlp["exponentialra0.25"])

corr03 =hlp["mean"].corr(hlp["exponentialra0.3"])
print("correaltion exp не послідовне 1")

print("{}\n{}\n{}\n{}\n{}".format(corr01, corr15, corr02, corr025, corr03))



turning_pointexp1 = turning_points(hlp["exponentialra0.1"],  n)

turning_pointsexp15= turning_points(hlp["exponentialra0.15"],  n)

turning_pointexp2_ = turning_points(hlp["exponentialra0.2"],  n)

turning_pointexp25= turning_points(hlp["exponentialra0.25"],  n)

turning_pointexp3 = turning_points(hlp["exponentialra0.3"],  n)

print("exp поворотні точки не послідовне {}\t{}\t{}\t{}\t{}".format(turning_pointexp1, turning_pointsexp15,turning_pointexp2_,turning_pointexp25,turning_pointexp3,))
