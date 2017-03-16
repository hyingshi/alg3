###############################################################################
# Yingshi Huang, Annie Lei
# CS 325
# Implementation 3
# Warm up problem: line of best fit
###############################################################################

import pulp
import csv
from math import pi, cos, sin

season_const = 2 * pi / 365.25
solar_const = season_const / 10.7

tempChange = pulp.LpProblem("Corvallis Temperature Change", pulp.LpMinimize)

M = pulp.LpVariable('M', 0)
x0 = pulp.LpVariable('x0', 0)
x1 = pulp.LpVariable('x1', 0)
x2 = pulp.LpVariable('x2', 0)
x3 = pulp.LpVariable('x3', 0)
x4 = pulp.LpVariable('x4', 0)
x5 = pulp.LpVariable('x5', 0)

# Objective function
tempChange += M, 'M'

# Constraints:
with open('Corvallis.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        if row[0] != 'STATION':             # skip header
            T = float(row[7])
            d = int(row[8])
    
            tempChange += x0 + x1*d + x2*cos(season_const*d) + x3*sin(season_const*d) + x4*cos(solar_const*d) + x5*sin(solar_const*d) - T <= M
            tempChange += x0 + x1*d + x2*cos(season_const*d) + x3*sin(season_const*d) + x4*cos(solar_const*d) + x5*sin(solar_const*d) - T >= -M

csvfile.close()

# print(tempChange)
tempChange.solve()                          # solve problem
print(pulp.LpStatus[tempChange.status])     # was optimal found?

# print the found values of x0, x1, ..., x5
for var in tempChange.variables():
    print("{} = {}".format(var.name, var.varValue))
