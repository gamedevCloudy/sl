from graph import Graph

def kruskal_mst(graph):
    edges = sorted([(cost, src, dest) for src, dest, cost in graph.get_all_edges()])
    mst_edges = []
    parent = {vertex: vertex for vertex in graph.get_vertices()}

    def find_set(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find_set(parent[vertex])
        return parent[vertex]

    def union_sets(u, v):
        root_u, root_v = find_set(u), find_set(v)
        parent[root_u] = root_v

    for cost, src, dest in edges:
        if find_set(src) != find_set(dest):
            mst_edges.append((src, dest, cost))
            union_sets(src, dest)

    return mst_edges

# Example usage:
g_kruskal = Graph()
g_kruskal.add_edge('A', 'B', 1)
g_kruskal.add_edge('A', 'C', 2)
g_kruskal.add_edge('B', 'C', 3)
g_kruskal.add_edge('B', 'D', 1)
g_kruskal.add_edge('C', 'D', 4)

mst_kruskal = kruskal_mst(g_kruskal)
print("Kruskal's Minimal Spanning Tree:")
print(mst_kruskal)
