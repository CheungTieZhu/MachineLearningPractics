import numpy as np
from sklearn.decomposition import FastICA

def calculate(data):
    ica = FastICA(n_components=8)
    ica.fit(data)
    AfterICA = ica.transform(data)
    return AfterICA