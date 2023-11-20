from collections import deque
from graph import Graph

def dijkstra(graph, start):
    visited = set()
    distances = {vertex: float('inf') for vertex in graph.get_vertices()}
    distances[start] = 0
    pq = deque([(0, start)])

    while pq:
        current_dist, current_vertex = pq.popleft()

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor in graph.get_neighbors(current_vertex):
            new_dist = distances[current_vertex] + 1  # Assuming unweighted graph

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                pq.append((new_dist, neighbor))

    return distances

# Example usage:
g_dijkstra = Graph()
g_dijkstra.add_edge(1, 2)
g_dijkstra.add_edge(1, 3)
g_dijkstra.add_edge(2, 4)
g_dijkstra.add_edge(2, 5)
g_dijkstra.add_edge(3, 6)

start_vertex_dijkstra = 1
shortest_paths = dijkstra(g_dijkstra, start_vertex_dijkstra)
print("Shortest Paths from Vertex", start_vertex_dijkstra)
print(shortest_paths)
