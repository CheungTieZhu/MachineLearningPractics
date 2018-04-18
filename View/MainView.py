from Controller.readFile import readMeterTXT
from Controller.PCAMethod import PCAMethod
from Controller.ICAMethod import ICAMethod
from Servers.LogisticRegression import LRClassifier
from Servers.SVMClassifier import SVMClassifier
from Servers.NeuronNetwork import NeuralNetworkClassifier
import numpy as np

def mainView():
    MeterA, MeterB, MeterC, MeterD = readMeterTXT()
    print("============Welcome to Ultrasonic Flowmeter diagnostics=================")
    print("========================================================================")
    print("=====================1.Meter A diagnostics =============================")
    print("=====================2.Meter B diagnostics =============================")
    print("=====================3.Meter C diagnostics =============================")
    print("=====================4.Meter D diagnostics =============================")
    print("========================================================================")
    selected = input("Please Select the Flowmeter to diagnosis:")
    if selected == "1":
        FlowMeter(MeterA,"A")
    elif selected == "2":
        FlowMeter(MeterB,"B")
    elif selected == "3":
        FlowMeter(MeterC,"C")
    elif selected == "4":
        FlowMeter(MeterD,"D")
    else:
        print("please select correct item!")
        mainView()

def FlowMeter(Parameter,category):
    if category == "A":
        Parameter = np.delete(Parameter,19,1)
    elif category =="B":
        Parameter = np.delete(Parameter, 13, 1)
    else:
        Parameter = Parameter
    print("===========Dimension Reduction==============")
    print("================1.PCA=======================")
    print("================2.ICA=======================")
    selected = input("please select item:")
    if selected == "1":
        data, y = PCAMethod(Parameter)
        classifierSelect(data, y)
    elif selected == "2":
        data, y = ICAMethod(Parameter)
        classifierSelect(data, y)
    else:
        print("please select correct item!")
        mainView()

def classifierSelect(data,y):

    print("================Classifier==================")
    print("================1.Logistic Regression=======")
    print("================2.SVM=======================")
    print("================3.Neuron Network============")
    selected = input("please select item:")
    if selected == "1":
        LRClassifier(data, y)
        mainView()
    elif selected == "2":
        SVMClassifier(data,y)
        mainView()
    elif selected == "3":
        NeuralNetworkClassifier(data,y)
        mainView()
    else:
        print("please select correct item!")
        mainView()



