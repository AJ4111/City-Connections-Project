City Connections Project - CSCI 311 Spring 2026

HOW TO RUN:
python main.py inputfile outputfile

Example:
python main.py OL.cedge.txt output.txt

DESCRIPTION:
This program computes a Minimum Spanning Tree (MST) for a given graph. 
We implemented two algorithms: Kruskal’s algorithm and Prim’s algorithm.
The goal is to connect all nodes with the minimum total edge weight.

FILES:
main.py         - main program; reads input, runs MST algorithm, writes output
kruskal.py      - Kruskal’s algorithm implementation using Union-Find
prim.py         - Prim’s algorithm implementation
graph_utils.py  - functions for reading graph data and building structures

INPUT FORMAT:
Each line represents one edge:
edgeID startNode endNode weight

Lines starting with '#' are comments and are ignored.

OUTPUT FORMAT:
Same as input format, but only includes edges selected for the MST.

DEPENDENCIES:
Python 3 (no external libraries required)
