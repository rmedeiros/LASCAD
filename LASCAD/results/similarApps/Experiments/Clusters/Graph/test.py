from pyvis.network import Network
import networkx as nx
import csv
import re
import random

f1 = open('minimumSpanningTree.txt','r')

c1 = csv.reader(f1, delimiter=' ')
edges = []
nodes = set()
for row in c1:
    for i in range(1,len(row)):
        nodes.add(row[0])
        nodes.add(row[1])
        edges.append( {"from":row[0], "to":row[1], "weight": row[2] , "label":str(round(float(row[2]),2))})



nt = Network("2000px", "2000px",directed=False)
colors= ["#585858" + hex(round((int(node.split('-')[-1])+1)*5*255/100)).split('x')[-1] for node in nodes]
nt.add_nodes(nodes=list(nodes), color=colors)
for edge in edges:
    nt.add_edge(edge['from'], edge['to'], width=float(edge['weight'])*5, label=edge['label'])
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
      "avoidOverlap": 0.72
    },
    "minVelocity": 0.75
  }
}'''
nt.set_options(options)
#nt.show_buttons()
nt.show("nx.html")
