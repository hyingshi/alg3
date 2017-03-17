import matplotlib as mlp
mlp.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import pulp
from math import pi
import csv
temperature = []
day = []

with open('Birmingham_clean.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # row[0] is STATION; row[1] is DATE; ...; row[7] is average (T),
        # row[8] is day (d)
        if row[0] != 'STATION':
            T = float(row[3])
            d = int(row[6])
            temperature.append(T)
            day.append(d)

csvfile.close()

plt.figure(num=1, figsize=(20,10))
plt.title('Daily Average Temperature Change in Birmingham since 1960')
plt.ylabel('Average temperature for given day (Celsius)')
plt.xlabel('Days (since Match 15, 1960)')

x = np.arange(21000)
y = 9.4971916 + 0.00016689454 * x  + 6.4061958 *np.sin(2 * np.pi * x / 365.25) 
plt.plot(x, y,linewidth = 3.3)

x = np.arange(21000)
y = 9.4971916 + 0.00016689454 * x 
plt.plot(x, y,linewidth = 3.3,color = 'g' )

plt.plot(day,temperature , 'ro',markersize = 2)
plt.axis([0, 21000, -15, 35])
plt.savefig("Bonus.png")
