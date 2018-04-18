import numpy as np
import Servers.calculatePCA as PCA



def PCAMethod(data):
# pca method for meterA
    y = data[:,len(data[0])-1]
    a = np.delete(data,len(data[0])-1,1)
    afterPCA = PCA.calculate(a)
    return afterPCA,y
