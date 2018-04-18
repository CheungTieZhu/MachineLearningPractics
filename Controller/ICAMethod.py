import numpy as np
import Servers.CalculateICA as ICA

def ICAMethod(data):
    # ica method for meterA
    y = data[:, len(data[0]) - 1]
    a = np.delete(data, len(data[0]) - 1, 1)
    a = np.delete(a, 19, 1)
    afterICA = ICA.calculate(a)
    return afterICA, y