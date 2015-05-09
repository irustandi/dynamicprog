__author__ = 'indra'

import numpy as np

stateValues = np.arange(0, 6)
x0 = 5

costFinal = [x ** 2 for x in stateValues]
costMat = np.zeros((4, 6))
costMat[3] = costFinal

controlMat = np.zeros((4, 6))

for k in np.arange(2, -1, -1):
    for state in stateValues:
        u = stateValues - state
        costNew = state ** 2 + u ** 2 + costMat[k+1]
        costMat[k, state] = np.min(costNew)
        index = np.argmin(costNew)
        controlMat[k, state] = u[index]