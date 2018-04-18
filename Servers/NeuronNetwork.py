from sklearn.neural_network import MLPClassifier
from sklearn.cross_validation import train_test_split

def NeuralNetworkClassifier(data,y):
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(data, y)
    classifier = MLPClassifier()
    classifier.fit(X_train_raw,y_train)
    predictions = classifier.predict(X_test_raw)
    correct = 0
    for i in range(0,len(predictions)):
        print('prediction：%s. ActualY:%s' % (predictions[i], y_test[i]))
        if y_test[i] == predictions[i]:
            correct += 1
    print("The correction rate:%2.f" %((correct/len(y_test))*100),"%")