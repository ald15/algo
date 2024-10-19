'''
BFS by ald15, 10.2024

input data: graph
'''


class Node:
    '''
    ## Simple Graph node
    '''
    def __init__(self, v: object, e: list[object] = None) -> None:
        self.v = v
        self.e = e if e is not None else []

    def add(self, e: list[object]) -> None:
        self.e += e


class Queue:
    '''
    ## Simple queue based on a list.
    It works slowly, but it is fast in coding
    and understanding algo.
    '''
    def __init__(self, elem: object = None) -> None:
        self.queue = []
        if elem is not None:
            self.put(elem)

    def put(self, elem: object) -> None:
        self.queue.append(elem)

    def get(self) -> object:
        return self.queue.pop(0)

    def empty(self) -> bool:
        return not len(self.queue)


def BFS(node1: Node, node2: Node) -> list[object]:
    '''
    ## Simple BFS algo
    An undirected graph
    '''
    Q = Queue(node1)
    visited = set([node1.v])
    prev = {node1.v: None}
    while not Q.empty():
        curNode = Q.get()
        if curNode == node2:
            temp, path = node2.v, [node2.v]
            while temp != node1.v:
                path.append(prev[temp])
                temp = prev[temp]
            return path[::-1]
        for edge in curNode.e:
            if edge.v not in visited:
                visited.add(edge.v)
                Q.put(edge)
                prev[edge.v] = curNode.v
    return []


# Test graph
N = 8  # Amount of vertex
V = [Node(i) for i in range(N)]  # graph - list of vertex
V[0].add([V[3], V[6]])
V[1].add([V[2], V[3], V[4]])
V[2].add([V[1], V[5]])
V[3].add([V[0], V[1], V[5]])
V[4].add([V[1], V[5], V[6]])
V[5].add([V[2], V[3], V[4]])
V[6].add([V[0], V[4]])
# V[7] is empty


# Examples
print(f' V_0 -> V_7 ? - {BFS(V[0], V[7])}')
print(f' V_0 -> V_4 ? - {BFS(V[0], V[4])}')
print(f' V_0 -> V_0 ? - {BFS(V[0], V[0])}')
