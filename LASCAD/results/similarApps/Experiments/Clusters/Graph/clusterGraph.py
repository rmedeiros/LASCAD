import networkx as nx
import matplotlib.pyplot as plt
import csv
import re
import os
from spanningtree import prim_mst_edges as ts
f1 = open('similarApps_showcase_noStem2_50_0.9_0.05.csv','r')

c1 = csv.reader(f1, delimiter=',')
pattern_feature = r'\'(.*?)\''
pattern_value = r'\((.*?)\,'
edges = ""
next(c1,None)
nodes = {}
for row in c1:
    for i in range(1,len(row)):
        col_value = float(re.search(pattern_value,row[i]).group(1))
        feature = re.search(pattern_feature,row[i]).group(1)
        if col_value <0.7:
            if col_value<0.1:
                weight=(col_value)*80
            elif col_value < 0.2:
                weight=(col_value)*65
            elif col_value < 0.3:
                weight=(col_value)*45
            elif col_value < 0.4:
                weight=(col_value)*25
            else:
                weight=(col_value)*10
            edges = edges + row[0]+","+feature+","+ str(1-col_value)+"\n"

f1 = open('edge_list.csv','w')
f1.write(edges)
f1.close()
G = nx.read_weighted_edgelist('minimumSpanningTree.txt', delimiter =" ")


# We have to set the population attribute for each of the 14 nodes
from networkx.algorithms import tree
mst = ts(G,False)
edgelist = list(mst)
print(e for e in edgelist)
nx.draw_networkx(G, with_labels = True)
plt.figure(figsize =(20, 10))

# node colour is a list of degrees of nodes

# size of node is a list of population of cities

edge_width = [0.0025 * G[u][v]['weight'] for u, v in G.edges()]
# width of edge is a list of weight of edges

nx.draw_networkx(G, alpha = 0.7,
                 with_labels = True, width = edge_width,
                 edge_color ='.4', cmap = plt.cm.Blues)

plt.axis('off')
plt.tight_layout()
plt.show()
