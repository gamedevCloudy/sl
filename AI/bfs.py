from graph import Graph
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

if __name__ == "__main__":
    # Example usage:
    # Create a graph
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    # Perform BFS starting from vertex 1
    print("Breadth-First Search:")
    bfs(g, 1)
