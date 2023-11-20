from graph import Graph
import heapq

def dijkstra_mst(graph, start):
    visited = set()
    distances = {vertex: float('inf') for vertex in graph.get_vertices()}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_vertex = heapq.heappop(pq)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, edge_weight in graph.get_edges(current_vertex):
            new_dist = distances[current_vertex] + edge_weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    mst_edges = []
    for vertex in graph.get_vertices():
        if vertex != start:
            mst_edges.append((vertex, graph.get_parent(vertex), distances[vertex]))

    return mst_edges

# Example usage:
g_dijkstra = Graph()
g_dijkstra.add_edge('A', 'B', 1)
g_dijkstra.add_edge('A', 'C', 2)
g_dijkstra.add_edge('B', 'C', 3)
g_dijkstra.add_edge('B', 'D', 1)
g_dijkstra.add_edge('C', 'D', 4)

start_vertex_dijkstra = 'A'
mst_dijkstra = dijkstra_mst(g_dijkstra, start_vertex_dijkstra)
print("Dijkstra's Minimal Spanning Tree:")
print(mst_dijkstra)
