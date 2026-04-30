class UnionFind:
    def __init__(self, nodes):
        self.parent = {}
        for node in nodes:
            self.parent[node] = node

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        self.parent[root_x] = root_y
        return True
    
def kruskal(edges, nodes):
    edges = sorted(edges, key = lambda e:e[3])
    uf = UnionFind(nodes)
    mst = []

    for edge in edges:
        edge_id, u, v, w = edge

        if uf.union(u, v):
            mst.append(edge)

        if len(mst) == len(nodes) - 1:
            break

    if len(mst) != len(nodes) - 1:
        print("Graph is not fully connected!")
    
    return mst

if __name__ == "__main__":
    edges = [
        (1, 1, 2, 4),
        (2, 1, 3, 2),
        (3, 2, 3, 1),
        (4, 2, 4, 5),
        (5, 3, 4, 3)
    ]
    nodes = {1, 2, 3, 4}

    mst = kruskal(edges, nodes)
    print(mst)