import numpy as np
import math
from sklearn.cross_validation import train_test_split

def begin(data,y):
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(data, y)
    meansArray = []
    stdArray = []
    correct = 0
    for i in range(0,len(X_train_raw.T)):
        means = np.mean(X_train_raw.T[i])
        meansArray.append(means)
        std = np.std(X_train_raw.T[i])
        stdArray.append(std)

    unique,prior = calculateProbability(y_train)

    for i in range(0,len(X_test_raw)):
        probability = np.array([])
        for j in range(0,len(prior)):
            p = 1
            for k in range(0,len(X_test_raw[1])):
                p *= prior[j]*calcProbDensity(X_test_raw[i,k],meansArray[k],stdArray[k])
            probability = np.append(probability,p)
        index = np.argmax(probability)
        if unique[index] == y_test[i]:
            correct += 1
        print(probability)
        print("prediction:", unique[index], "label:", y_test[i])
    print("the correct rate:",correct/len(y_test))

def calculateProbability(y):
    prior = np.array([])
    unique,count = np.unique(y,return_counts=True)
    for i in range(0,len(unique)):
        prior = np.append(prior,count[i]/len(y))
    return unique,prior

def calcProbDensity(test_X,meanLabel,stdLabel):
    return np.exp(-np.square(test_X-meanLabel)/(2.0*np.square(stdLabel)))/(np.sqrt(2.0*math.pi)*stdLabel)





