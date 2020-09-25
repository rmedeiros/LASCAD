from pyvis.network import Network
import networkx as nx
import csv
import re
import random

f1 = open('similarApps_showcase_noStem2_50_0.9_0.05.csv','r')

c1 = csv.reader(f1, delimiter=',')
pattern_feature = r'\'(.*?)\''
pattern_value = r'\((.*?)\,'
edges = []
next(c1,None)
nodes = set()
for row in c1:
    for i in range(1,len(row)):
        col_value = float(re.search(pattern_value,row[i]).group(1))
        feature = re.search(pattern_feature,row[i]).group(1)
        nodes.add(feature)
        if col_value <0.7:
            if col_value<0.1:
                weight=(1-col_value)*80
            elif col_value < 0.2:
                weight=(1-col_value)*65
            elif col_value < 0.3:
                weight=(1-col_value)*45
            elif col_value < 0.4:
                weight=(1-col_value)*25
            else:
                weight=(1-col_value)*10
            edges.append( {"from":row[0], "to":feature, "weight": weight , "label":str(round(1-col_value,2))})



nt = Network("2000px", "2000px")
colors= ["#"+ "%06x" % random.randint(0, 0xFFFFFF) for i in range(0,20)]
nt.add_nodes(nodes=list(nodes), color=colors)
for edge in edges:
    nt.add_edge(edge['from'], edge['to'], width= edge['weight'], label=edge['label'])
# populates the nodes and edges data structures
#nt.from_nx(nx_graph)
options = '''var options = {
  "edges": {
    "color": {
      "color": "rgba(132,132,132,0.34)",
      "highlight": "rgba(0,23,38,1)",
      "inherit": false
    },
    "smooth": false
  },
  "interaction": {
    "hoverConnectedEdges": false
  },
  "physics": {
    "barnesHut": {
      "springLength": 430,
      "avoidOverlap": 0.72
    },
    "minVelocity": 0.75
  }
}'''
nt.set_options(options)
#nt.show_buttons()
nt.show("nx.html")
