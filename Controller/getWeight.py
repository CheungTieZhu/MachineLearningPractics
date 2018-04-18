import Servers.LogisticRegression as LClassifier
def getWeight(data,y):
    return LClassifier.LogisticRegression(data.T, y)