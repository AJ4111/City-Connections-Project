from graph_utils import read_graph
from kruskal import kruskal
from prim import prim
import sys


input_file = sys.argv[1]
output_file = sys.argv[2]

edges, adj = read_graph(input_file)
nodes = set(adj.keys())

mst = kruskal(edges, nodes)
# mst = prim(nodes, adj)


with open(output_file, 'w') as f:
    for edge_id, u, v, w in mst:
        f.write(f"{edge_id} {u} {v} {w}\n")