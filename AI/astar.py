from graph import Graph
import heapq

class AStar:
    def __init__(self, graph):
        self.graph = graph

    def astar(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))  # Priority queue with (f, node) tuple
        came_from = {start: None}
        g_score = {start: 0}

        while open_set:
            current_g, current = heapq.heappop(open_set)

            if current == goal:
                path = self.reconstruct_path(came_from, goal)
                return path

            for neighbor in self.graph.get_neighbors(current):
                tentative_g = g_score[current] + 1  # Assuming unweighted graph

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))
                    came_from[neighbor] = current

        return None  # No path found

    def heuristic(self, node, goal):
        # Manhatten distance heuristic for simplicity (can be replaced with other heuristics)
        x1, y1 = node
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)

    def reconstruct_path(self, came_from, current):
        path = []
        while current is not None:
            path.append(current)
            current = came_from[current]
        return path[::-1]

# Example usage:
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    g.add_edge((0, 0), (0, 1))
    g.add_edge((0, 1), (1, 1))
    g.add_edge((1, 1), (1, 0))
    g.add_edge((1, 0), (0, 0))
    g.add_edge((0, 1), (0, 2))
    g.add_edge((0, 2), (1, 2))
    g.add_edge((1, 2), (1, 1))

    # Define start and goal nodes
    start_node = (0, 0)
    goal_node = (1, 2)

    # Create AStar object and find the path
    astar = AStar(g)
    path = astar.astar(start_node, goal_node)

    if path:
        print(f"A* Path from {start_node} to {goal_node}: {path}")
    else:
        print("No path found.")
