###############################################################################
# Yingshi Huang, Annie Lei
# CS 325
# Implementation 3
# Warm up problem: line of best fit
###############################################################################

import pulp

points = [[1,3], [2,5], [3,7], [5,11], [7,14], [8,15], [10,19]]

bestFit = pulp.LpProblem("Line of best fit", pulp.LpMinimize)

M = pulp.LpVariable('M', 0)
a = pulp.LpVariable('a', 0)
b = pulp.LpVariable('b', 0)

# Objective function
bestFit += M, 'M'

# Constraints: 7 pairs --> 14 total constraints
for point in points:
    bestFit += a * point[0] + b - point[1] <= M
    bestFit += a * point[0] + b - point[1] >= -M

print(points)                           # print points
print(bestFit)                          # print constraints
bestFit.solve()                         # solve problem
print(pulp.LpStatus[bestFit.status])    # was optimal found?

# print the found values of ``a`` and ``b``
for var in bestFit.variables():
    print("{} = {}".format(var.name, var.varValue))
