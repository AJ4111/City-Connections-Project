# min-priority queue
class MinPriorityQueue:
    """
    Min-heap priority queue.
    Mantains a position dictionary so any node can be located in the heap at O(1).
    """

    def __init__(self):
        self.heap = []
        self.position = {}

    def insert(self, node, distance):
        """
        Add new node with given priority key.
        Appends to the end of the heap and sifts up to restore property.
        """
        entry = [distance, node]
        self.position[node] = len(self.heap)
        self.heap.append(entry)
        self._sift_up(len(self.heap) - 1)

    def update(self, node, new_distance):
        """
        Decrease priority key of a node.
        Looks up node's index and updates its key in place.
        """
        ind = self.position[node]
        self.heap[ind][0] = new_distance
        self._sift_up(ind)

    def extract_min(self):
        """
        Removes and returns node with smallest key in heap.
        Swaps root with last element, then pop, and sifts the new root down.
        """
        self._swap(0, len(self.heap) - 1)
        min_entry = self.heap.pop()
        self.position.pop(min_entry[1], None)
        if self.heap:
            self._sift_down(0)
        return min_entry[1], min_entry[0]
    
    def is_in(self, node):
        """
        Checks if node is currently in priority queue.
        """
        return node in self.position
    
    def is_empty(self):
        """
        Checks if queue is empty.
        """
        return len(self.heap) == 0
    
    def _swap(self, i, j):
        """
        Swaps heap entries at index i and j.
        """
        self.position[self.heap[i][1]] = j
        self.position[self.heap[j][1]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, i):
        """
        Move entry at index i up the heap until the min-heap property is restored.
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
        Move entry at index i down the heap until the min-heap property is restored.
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
    
def prim(nodes, adjacency_list):
    """
    Computes MST using Prim's algorithm.

    Args:
            nodes: set of nodes in graph
            adjacency_list: dictionary mapping node to a list of (neighbor, weight, edge_id)
    
    Return:
            list of tuples forming mst in the order edges were added.
            empty if there are no nodes or graph is disconnected before nodes are reached.
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

