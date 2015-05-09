__author__ = 'indra'

import numpy as np

stateValues = np.arange(0, 6)
x0 = 5

costMat = np.zeros((5, 6))
costMat[4] = np.inf
costMat[4, 5] = 25

controlMat = np.zeros((5, 6))

for k in np.arange(3, -1, -1):
    for state in stateValues:
        u = stateValues - state
        costNew = state ** 2 + u ** 2 + costMat[k+1]
        costMat[k, state] = np.min(costNew)
        index = np.argmin(costNew)
        controlMat[k, state] = u[index]