#djikstra algorithm

import sys
import math
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_graph(self):
        for i in range(self.V):
            for j in range(self.V):
                print(self.graph[i][j], end=" ")
            print("")

    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    def djikstra(self, src, dest):
        dist = [math.inf] * self.V
        dist[src] = 0
        heap = []
        heapq.heappush(heap, (0, src))
        while heap:
            u = heapq.heappop(heap)[1]
            for v in range(self.V):
                if self.graph[u][v] > 0 and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    heapq.heappush(heap, (dist[v], v))
        return dist[dest]

    def Floyd(self, src, dest):
        dist = [[math.inf for x in range(self.V)] for y in range(self.V)]
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] > 0:
                    dist[i][j] = self.graph[i][j]
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist[src][dest]
    
    #ballman ford
    def Ballman_Ford(self, src, dest):
        dist = [math.inf] * self.V
        dist[src] = 0
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] > 0 and dist[j] > dist[i] + self.graph[i][j]:
                    dist[j] = dist[i] + self.graph[i][j]
        return dist[dest]


def main():
    V = 7
    graph = Graph(V)
    graph.add_edge(1, 2, 7)
    graph.add_edge(1, 3, 9)
    graph.add_edge(1, 6, 14)
    graph.add_edge(2, 3, 10)
    graph.add_edge(2, 4, 15)
    graph.add_edge(3, 4, 11)
    graph.add_edge(3, 6, 2)
    graph.add_edge(6, 5, 9)
    graph.add_edge(4, 5, 6)

    print(graph.djikstra(1, 5))
    print(graph.Floyd(1, 5))
    print(graph.Ballman_Ford(1, 5))

main()