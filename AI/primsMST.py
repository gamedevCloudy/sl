from graph import Graph
import heapq

def prim_mst(graph):
    start_vertex = list(graph.get_vertices())[0]
    visited = set([start_vertex])
    edges = [
        (cost, start_vertex, neighbor)
        for neighbor, cost in graph.get_edges(start_vertex)
    ]
    heapq.heapify(edges)
    mst_edges = []

    while edges:
        cost, src, dest = heapq.heappop(edges)
        if dest not in visited:
            visited.add(dest)
            mst_edges.append((src, dest, cost))
            for neighbor, cost in graph.get_edges(dest):
                if neighbor not in visited:
                    heapq.heappush(edges, (cost, dest, neighbor))

    return mst_edges

# Example usage:
g_prim = Graph()
g_prim.add_edge('A', 'B', 1)
g_prim.add_edge('A', 'C', 2)
g_prim.add_edge('B', 'C', 3)
g_prim.add_edge('B', 'D', 1)
g_prim.add_edge('C', 'D', 4)

mst_prim = prim_mst(g_prim)
print("Prim's Minimal Spanning Tree:")
print(mst_prim)
