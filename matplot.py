import urllib
import json
from matplotlib import pyplot as plt

fhand = urllib.request.urlopen("http://climatedataapi.worldbank.org/climateweb/rest/v1/country/annualavg/tas/1980/1999/IND")
info = json.load(fhand)
fromYear = info[0]["fromYear"]
AVG_annual = []
length = len(info)
Years = []
for p in range(length):
    Years.append(fromYear+p)
    AVG_annual=info[p]["annualData"]+AVG_annual

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(Years,AVG_annual, color='r')

ax2 = fig.add_subplot(222)
ax2.bar(Years, AVG_annual, color='tomato', linewidth=0.1)

ay1 = fig.add_subplot(223)
ay1.scatter(Years, AVG_annual, color='crimson', lw=0.1)

ay2 = fig.add_subplot(224)
ay2.stackplot(Years, AVG_annual, color='salmon')

plt.show()