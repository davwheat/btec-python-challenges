# Energy bill calculator problem
# 3 points

import math

calorificValue = 39.3
# pounds per kwh
energyCost = 0.0284

# Return cost in pounds for the amount of energy used
def GetCost(previousReading, currentReading, calorificValue):
    unitsUsed = currentReading - previousReading
    kwhUsed = unitsUsed * 1.022 * calorificValue / 3.6

    costInPounds = kwhUsed * energyCost

    # return math.ceil(costInPounds * 100) / 100
    return costInPounds


# print("£" + str(GetCost(100, 200, calorificValue)))
