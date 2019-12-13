import math
import pandas as pd


def object_prop(dat):
    fstlevel = dict()
    fstlevel["sum"] = dat.sum()
    fstlevel["mean"] =dat.mean()
    fstlevel["max"] = dat.max()

    fstlevel["min"] = dat.min()

    fstlevel["median"] = dat.median()

    fstlevel["mode"] = dat.mode()

    fstlevel["count"] = dat.count()

    fstlevel["skrew"] = dat.skew()

    fstlevel["kurt"] = dat.kurt()

    fstlevel["standart deviation"] = dat.std()

    fstlevel["standart error"] = fstlevel["standart deviation"] / math.sqrt(dat.__len__())

    fstlevel["sample variation"] = dat.var()

    return pd.DataFrame(fstlevel)

