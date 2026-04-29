City Connections Project - CSCI 311 Spring 2026

HOW TO RUN:
python main.py inputfile outputfile

FILES:
graph_utils.py  - file reader, adjacency list builder, file writer, union-find, min-heap
main.py         - entry point, ties everything together

INPUT FORMAT:
Each line: edgeID startNode endNode weight
Lines starting with # are comments and are ignored

OUTPUT FORMAT:
Same as input — only the edges selected for the MST

DEPENDENCIES:
Python 3 only, no external libraries
