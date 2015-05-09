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
        wplus = np.zeros(np.size(u))
        wplus[1:5.] = 1
        wmin = np.zeros(np.size(u))
        wmin[1:5.] = -1

        stateNextPlus = stateValues + wplus
        stateNextMin = stateValues + wmin

        costNewPlus = state ** 2 + u ** 2 + costMat[k+1, np.int_(stateNextPlus)]
        costNewMin = state ** 2 + u ** 2 + costMat[k+1, np.int_(stateNextMin)]
        costMat[k, state] = 0.5 * np.min(costNewPlus) + 0.5 * np.min(costNewMin)
        index = np.argmin(0.5 * costNewPlus + 0.5 * costNewMin)
        controlMat[k, state] = u[index]