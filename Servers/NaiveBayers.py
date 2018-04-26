import numpy as np
from sklearn.cross_validation import train_test_split

def calculateMeans(data,y):
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(data, y)
    bayesArray = []
    meansArray = []
    correct = 0
    a = 1
    for i in range(0,len(X_train_raw.T)):
        means = np.mean(X_train_raw.T[i])
        result,y1 = calculateProbability(X_train_raw.T[i],means,y_train)
        bayesArray.append(result)
        meansArray.append(means)

    for i in range(0,len(X_test_raw)):
        for k in range(0,len(X_test_raw[1])):
             if X_test_raw.T[k,i] < meansArray[k]:
                 probability = bayesArray[k][1]
                 a *= probability
             else:
                 probability = bayesArray[k][0]
                 a *= probability
        position = np.argmax(a)
        if y_test[i] == y1[position]:
            correct += 1
        print("prediction:",y1[position],"label:",y_test[i])
    print("the correct rate:",correct/len(y_test))

def calculateProbability(data,means,y):
    result = []
    resultProbabilityYes = np.array([])
    resultProbabilityNo = np.array([])
    resultYes = np.array([])
    resultNo = np.array([])
    for i in range(0,len(data)):
        if data[i] >= means:
            resultYes = np.append(resultYes,y[i])
        else:
            resultNo = np.append(resultNo,y[i])
    unique = np.unique(y)
    uniqueYes,countsY = np.unique(resultYes,return_counts=True)
    uniqueNo,countsN = np.unique(resultNo,return_counts=True)

    for i in range(0,len(unique)):
        try:
            if unique[i] != uniqueYes[i]:
                uniqueYes = np.insert(uniqueYes,i,unique[i])
                countsY = np.insert(countsY,i,0)
        except:
            uniqueYes = np.insert(uniqueYes, i, unique[i])
            countsY = np.insert(countsY, i, 0)


    for i in range(0,len(unique)):
        try:
            if unique[i] != uniqueNo[i]:
                uniqueNo = np.insert(uniqueNo,i,unique[i])
                countsN = np.insert(countsN,i,0)
        except:
            uniqueNo = np.insert(uniqueNo, i, unique[i])
            countsN = np.insert(countsN, i, 0)

    for i in range(0,len(unique)):
        resultProbabilityYes = np.append(resultProbabilityYes,countsY[i]/len(resultYes))

    for i in range(0,len(unique)):
        resultProbabilityNo = np.append(resultProbabilityNo,countsN[i]/len(resultNo))

    result.append(resultProbabilityYes)
    result.append(resultProbabilityNo)

    return result,uniqueNo




