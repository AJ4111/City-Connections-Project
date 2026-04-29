def read_graph(filename):
    edges = []
    adjacency_list = {}

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or line == '':
                continue
            
            parts = line.split()
            edge_id = int(parts[0])
            start = int(parts[1])
            end = int(parts[2])
            weight = float(parts[3])

            edges.append((edge_id, start, end, weight))

            if start not in adjacency_list:
                adjacency_list[start] = []
            if end not in adjacency_list:
                adjacency_list[end] = []

            adjacency_list[start].append((end, weight, edge_id))
            adjacency_list[end].append((start, weight, edge_id))

    return edges, adjacency_list


