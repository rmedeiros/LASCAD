
import csv

f1 = open('../../similarApps_showcase_noStem2_150_0.8_0.2.csv', 'r')
f2 = open('groundTruth.csv', 'r')

c1 = csv.reader(f1, delimiter=',')
c2 = csv.reader(f2, delimiter=',')
master_list = list(c2)
pattern = r'\'(.*?)\''
aggregated_recall=0
positives=0
total=0
recall=0.0
pattern = r'\'(.*?)\''
next(c1,None)
import re
for row in c1:
    for feature in master_list:
        if feature[0]==row[0]:
            for i in range(1,6):
                row_col= re.search(pattern,row[i]).group(1).replace("\'","")
                if row_col in [feature[i] for i in range(1,6)]:
                    positives=positives+1
            recall = recall + (positives/5)
            print(feature[0] +":"+ str(positives))
            positives=0
            total=total+1
            break
total_recall = recall/total
print(total)
print("The obtained recall is: "+ str(total_recall))



