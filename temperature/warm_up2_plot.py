import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import pulp
from math import pi
import csv
temperature = []
day = []

with open('Corvallis.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        # row[0] is STATION; row[1] is DATE; ...; row[7] is average (T),
        # row[8] is day (d)
		if row[0] != 'STATION':
			T = float(row[7])
			d = int(row[8])
			temperature.append(T)
			day.append(d)
   
csvfile.close()

plt.figure(num=1, figsize=(20,10))
plt.title('Daily Average Temperature Change in Corvallis Since 1952')
plt.ylabel('Average temperature for given day (Celsius)')
plt.xlabel('Days (since May 1, 1952)')

x = np.arange(22500)
y = 7.5576509 + 0.00023193925 * x + 4.9302661 * np.cos(2 * np.pi * x / 365.25) + 8.4965901 * np.sin(2 * np.pi * x / 365.25)
plt.plot(x, y,linewidth = 3.3)

x = np.arange(22500)
y = 7.5576509 + 0.00023193925 * x 
plt.plot(x, y,linewidth = 3.3,color = 'g' )

plt.plot(day,temperature , 'ro',markersize = 2)
plt.axis([0, 22500, -15, 35])
plt.savefig("warmUp2.png")
