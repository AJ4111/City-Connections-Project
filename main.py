from graph_utils import read_graph
from kruskal import kruskal
from prim import prim
import sys

import time

input_file = sys.argv[1]
output_file = sys.argv[2]

edges, adj = read_graph(input_file)
nodes = set(adj.keys())

# timing of algorithms
start = time.time()
mst = kruskal(edges, nodes)
kruskal_time = time.time() - start

start = time.time()
mst = prim(nodes, adj)
prim_time = time.time() - start

print(f"kruskal: {kruskal_time * 1000:4f} ms")
print(f"prim: {prim_time * 1000:4f} ms")

with open(output_file, 'w') as f:
    for edge_id, u, v, w in mst:
        f.write(f"{edge_id} {u} {v} {w}\n")