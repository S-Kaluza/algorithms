class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node


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
    V = 10
    graph = Graph(V)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 8)
    graph.add_edge(3, 6)
    graph.add_edge(6, 5)
    graph.add_edge(5, 2)
    graph.add_edge(9, 1)
    graph.add_edge(8, 1)
    graph.print_graph()
    graph.print_matrix()

main()