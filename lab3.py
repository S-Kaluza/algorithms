from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DisjointSet:
    def __init__(self, vertices):
        self.V = vertices
        self.parent = [i for i in range(self.V)]
        self.rank = [0] * self.V

    def find(self, node):
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
    
    def isConnected(self, node1, node2):
        return self.find(node1) == self.find(node2)

def top_sort(graph):
    sorted_nodes, visited = deque(), set()
    for node in graph.keys():
        if node not in visited:
           dfs(graph, node, visited, sorted_nodes)
    return list(sorted_nodes)
 
def dfs(graph, start_node, visited, sorted_nodes):
    visited.add(start_node)
    if start_node in graph:
        neighbors = graph[start_node]
        for neighbor in neighbors:
            if neighbor not in visited:
                dfs(graph, neighbor, visited, sorted_nodes)
    sorted_nodes.appendleft(start_node)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, src, dest):
        if src in self.graph:
            self.graph[src].append(dest)
        else:
            self.graph[src] = [dest]

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print("")

    def print_matrix(self):
        matrix = [[0 for x in range(self.V)] for y in range(self.V)]
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                matrix[i][temp.data] = 1
                temp = temp.next
        for i in range(self.V):
            for j in range(self.V):
                if(i != 0 and j != 0):
                    print(matrix[i][j], end=" ")
            print("")



def main():
    ds = DisjointSet(11)
    ds.union(10, 8)
    ds.union(3, 1)
    ds.union(8, 9)
    ds.union(1, 5)
    ds.union(5, 7)
    ds.union(2, 6)
    ds.union(6, 4)
    ds.union(6, 5)
    print(ds.isConnected(10, 7))
    print(ds.isConnected(10, 9))
    print(ds.isConnected(3, 4))

    V = 10
    graph = Graph(V)
    graph.add_edge(1, 4)
    graph.add_edge(1, 5)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(3, 8)
    graph.add_edge(4, 6)
    graph.add_edge(4, 7)
    graph.add_edge(4, 8)
    graph.add_edge(5, 7)

    sorted_nodes = top_sort(graph.graph)
    print(sorted_nodes)

    graph = graphWithWeight(6)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 3, 4)
    graph.add_edge(3, 4, 2)

    edges = prim(graph, 0)
    print(edges)

main()