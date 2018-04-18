import numpy as np
from sklearn.decomposition import PCA

def proveRedundance(data,begin,end):
    sum = 0
    error = 0
    for j in range(0,len(data)):
        for i in range(begin,end):
            sum += data[j,i]
        b = sum/8
# the error less than 0.000002 will regard as the sum value
        if round(sum/(begin-end),6) - data[j,end] > 0.000002:
            error +=1
        sum = 0
    if error > 0:
        return False
    else:
        return True

def calculate(data):
    pca = PCA(n_components=5)
    pca.fit(data)
    AfterPCA = pca.transform(data)
    return AfterPCA

def feartureKeep(evalue,percentage):
    sortArray = np.sort(evalue)
    sortArray = sortArray[-1::-1]
    arraySum = sum(sortArray)
    tempsum = 0
    num = 0
    for i in sortArray:
        tempsum += i
        num += 1
        if tempsum >= arraySum * percentage:
            return num





