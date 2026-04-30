class UnionFind:
    def __init__(self, nodes):
        self.parent = {}
        self.rank = {}

        for node in nodes:
            self.parent[node] = node
            self.rank[node] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def kruskal(edges, nodes):
    edges = sorted(edges, key=lambda e: e[3])
    uf = UnionFind(nodes)
    mst = []

    for edge in edges:
        edge_id, u, v, w = edge

        if uf.union(u, v):
            mst.append(edge)

        if len(mst) == len(nodes) - 1:
            break
    
    return mst