class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[vertex].append(neighbor)
        self.graph[neighbor].append(vertex)

    def get_neighbors(self, vertex):
        return self.graph[vertex]

    def get_vertices(self):
        return list(self.graph.keys())
 