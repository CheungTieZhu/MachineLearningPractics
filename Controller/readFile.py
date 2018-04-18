import numpy as np
def readMeterTXT():

    meterATxt = np.loadtxt("./Flowmeters/Meter A.txt")
    meterBTxt = np.loadtxt("./Flowmeters/Meter B.txt")
    meterCTxt = np.loadtxt("./Flowmeters/Meter C.txt")
    meterDTxt = np.loadtxt("./Flowmeters/Meter D.txt")

    return meterATxt,meterBTxt,meterCTxt,meterDTxt


