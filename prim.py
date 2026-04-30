# min-priority queue
class MinPriorityQueue:
    """
    docstring
    """

    def __init__(self):
        self.heap = []
        self.position = {}

    def insert(self, node, distance):
        """
        insert docstring
        """
        entry = [distance, node]
        self.position[node] = len(self.heap)
        self.heap.append(entry)
        self.heap.append(entry)
        self._sift_up(len(self.heap) - 1)

    def update(self, node, new_distance):
        """
        decrease docstring
        """
        ind = self.position[node]
        self.heap[ind][0] = new_distance
        self._sift_up(ind)

    def extract_min(self):
        """
        docstring
        """
        self._swap(0, len(self.heap) - 1)
        min_entry = self.heap.pop()
        self.position.pop(min_entry[1], None)
        if self.heap:
            self._sift_down(0)
        return min_entry[1], min_entry[0]
    
    def is_in(self, node):
        """
        docstring
        """
        return node in self.position
    
    def is_empty(self):
        """
        docstring
        """
        return len(self.heap) == 0
    
    def _swap(self, i, j):
        """
        docstring
        """
        self.position[self.heap[i][1]] = j
        self.position[self.heap[j][1]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, i):
        """
        docstring
        """
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] < self.heap[parent][0]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i):
        """
        docstring
        """
        n = len(self.heap)
        left = 2 * i + 1

        while left < n:
            right = left + 1
            smallest = i

            if self.heap[left][0] < self.heap[i][0]:
                smallest = left
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            
            if smallest == i:
                break

            self._swap(i, smallest)
            i = smallest
            left = 2 * i + 1
    
def prim(edges, nodes, adjacency_list):
    """
    docstring
    """
    if not nodes:
        return []
    
    distances = {node: float('inf') for node in nodes}
    edge = {} # (edge_id, u, v, weight) node
    S = set() # set of vertices

    pq = MinPriorityQueue()
    start = min(nodes)

    for node in nodes:
        distances[node] = 0 if node == start else float('inf')
        pq.insert(node, distances[node])

    mst = []

    while not pq.is_empty() and len(mst) < len(nodes) - 1:
        v, d = pq.extract_min()

        if d == float('inf'):
            break

        S.add(v)

        if v in edge:
            mst.append(edge[v])

        for neighbor, weight, edge_id in adjacency_list[v]:
            if neighbor not in S and weight < distances[neighbor]:
                distances[neighbor] = weight
                edge[neighbor] = (edge_id, v, neighbor, weight)
                pq.update(neighbor, weight)

    return mst

