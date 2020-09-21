import csv

import matplotlib.pyplot as plt

f1 = open('similarApps_showcase_noStem2_150_0.8_0.2_terms.csv', 'r')

c1 = csv.reader(f1, delimiter=',')
pattern = r'\'(.*?)\''
positives=0
features = []
top1= []
pattern = r'\((.*?)\,'
next(c1,None)
import re
for row in c1:
    features.append(row[0])
    top1.append(float(re.search(pattern,row[1]).group(1)))

lists = sorted(zip(*[top1, features]),reverse=True)
y, x = list(zip(*lists))

plt.plot(x, y)
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)
ax.plot(x, y, 'bo-', linewidth=2, markersize=6)
plt.xticks(x, rotation='vertical')
plt.show()
fig.savefig("Lonely_features-terms")